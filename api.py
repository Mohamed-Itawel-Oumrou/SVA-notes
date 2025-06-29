# a mettre dans /var/lib/asterisk/note/
from flask import Flask, request, jsonify
import mysql.connector
app = Flask(__name__)
@app.route('/note', methods=['GET'])
def get_note():
    ext = request.args.get('extension')
    if not ext:
        return jsonify({"status": "error", "message": "Extension manquante"}), 400
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='passer',
            database='ecole'
        )
        cursor = conn.cursor()
        cursor.execute("SELECT note FROM notes WHERE extension = %s", (ext,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return jsonify({"status": "success", "note": row[0]})
        else:
            return jsonify({"status": "error", "message": "Aucune note trouvée"}), 404
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
