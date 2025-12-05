import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import pymysql

# -------- DB helpers --------
def get_conn():
    return pymysql.connect(
        host=os.getenv("MYSQL_HOST", ""),
        user=os.getenv("MYSQL_USER", "user"),
        password=os.getenv("MYSQL_PASSWORD", "pass"),
        database=os.getenv("MYSQL_DATABASE", "students"),
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=True,
        charset="utf8mb4"
    )


# -------- Fetch helpers --------
def fetch_departments():
    conn = get_conn()
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM dept ORDER BY major_id;")
        return cur.fetchall()


def fetch_origins():
    conn = get_conn()
    with conn.cursor() as cur:
        cur.execute("SELECT id, code FROM origin ORDER BY id;")
        return cur.fetchall()


def fetch_students():
    """
    Para la tabla (lista):
      - devolvemos major (texto) y origin (código),
        y también phone/email.
    """
    conn = get_conn()
    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT 
                s.id,
                s.name,
                d.major AS major,
                o.code AS origin,
                s.phone,
                s.email
            FROM students s
            JOIN dept d ON s.major_id = d.major_id
            JOIN origin o ON s.origin_id = o.id
            ORDER BY s.id;
            """
        )
        return cur.fetchall()


def fetch_student(student_id):
    """
    Para editar:
      - devolvemos major_id y origin_id (números)
        además de phone/email.
    """
    conn = get_conn()
    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT 
                id,
                name,
                major_id,
                origin_id,
                phone,
                email
            FROM students;
            """,
            (student_id,),
        )
        return cur.fetchone()


def create_student(name, major_id, origin_id, phone, email):
    conn = get_conn()
    with conn.cursor() as cur:
        cur.execute(
            """
            INSERT INTO students (name, major_id, origin_id, phone, email)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (name, major_id, origin_id, phone, email),
        )
        return cur.lastrowid


def update_student(student_id, name, major_id, origin_id, phone, email):
    conn = get_conn()
    with conn.cursor() as cur:
        cur.execute(
            """
            UPDATE students
            SET name = %s,
                major_id = %s,
                origin_id = %s,
                phone = %s,
                email = %s
            WHERE id = %s
            """,
            (name, major_id, origin_id, phone, email, student_id),
        )
        return cur.rowcount


def delete_student(student_id):
    conn = get_conn()
    with conn.cursor() as cur:
        cur.execute("DELETE FROM students WHERE id = %s", (student_id,))
        return cur.rowcount


# -------- Flask app --------
app = Flask(__name__, static_folder="static", static_url_path="")
CORS(app)


@app.route("/")
def root():
    return send_from_directory("static", "index.html")


# ======================
#   STUDENTS API
# ======================

# LISTA
@app.get("/api/students")
def api_list_students():
    try:
        data = fetch_students()
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# UNO SOLO (para Edit)
@app.get("/api/students/<int:student_id>")
def api_get_student(student_id):
    try:
        row = fetch_student(student_id)
        if not row:
            return jsonify({"error": "Not found"}), 404
        return jsonify(row), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# CREAR (Enroll)
@app.post("/api/students")
def api_create_student():
    try:
        data = request.get_json(force=True) or {}

        name = data.get("name")
        major_id = data.get("major_id")
        origin_id = data.get("origin_id")
        email = data.get("email")

        if not name or not major_id or not origin_id:
            return jsonify({"error": "name, major_id y origin_id son requeridos"}), 400

        try:
            major_id = int(major_id)
            origin_id = int(origin_id)
        except ValueError:
            return jsonify({"error": "major_id y origin_id deben ser enteros"}), 400

        new_id = create_student(name, major_id, origin_id, email)
        row = fetch_student(new_id)
        return jsonify(row), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# EDITAR
@app.put("/api/students/<int:student_id>")
def api_update_student(student_id):
    try:
        data = request.get_json(force=True) or {}

        name = data.get("name")
        major_id = data.get("major_id")
        origin_id = data.get("origin_id")
        phone = data.get("phone")
        email = data.get("email")

        if not name or not major_id or not origin_id:
            return jsonify({"error": "name, major_id y origin_id son requeridos"}), 400

        try:
            major_id = int(major_id)
            origin_id = int(origin_id)
        except ValueError:
            return jsonify({"error": "major_id y origin_id deben ser enteros"}), 400

        # Ver si existe
        if not fetch_student(student_id):
            return jsonify({"error": "Not found"}), 404

        changed = update_student(student_id, name, major_id, origin_id, phone, email)
        if changed == 0:
            return jsonify({"error": "Not found"}), 404

        row = fetch_student(student_id)
        return jsonify(row), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# BORRAR
@app.delete("/api/students/<int:student_id>")
def api_delete_student(student_id):
    try:
        deleted = delete_student(student_id)
        if deleted == 0:
            return jsonify({"error": "Not found"}), 404
        return jsonify({"message": "Deleted"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ======================
#   DEPARTMENTS / ORIGINS
# ======================
@app.get("/api/departments")
def api_departments():
    try:
        return jsonify(fetch_departments()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.get("/api/origins")
def api_origins():
    try:
        return jsonify(fetch_origins()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    app.run(host="0.0.0.0", port=port)
