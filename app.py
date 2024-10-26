from flask import Flask, render_template, request, jsonify
from databricks import sql
import os

app = Flask(__name__)

def get_warehouse_connection():
    try:
        return sql.connect(
            server_hostname = 'dbc-workspaceID.cloud.databricks.com',
            http_path       = '/sql/1.0/warehouses/93c9d7e2b186c421',
            access_token    = 'databricks access token'
        )
    except Exception as e:
        print(f"Error connecting to Databricks: {e}")
        raise

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        agent_id = request.form['agent_id']
        try:
            with get_warehouse_connection() as connection:
                with connection.cursor() as cursor:
                    # Get HCP count
                    cursor.execute(f"""
                        SELECT COUNT(*) as hcp_count 
                        FROM (
                            SELECT DISTINCT HCP_Name, Distance, Specialty, Preferred_Drug, Communication_Pref
                            FROM final_assigned_hcps 
                            WHERE Agent_ID = '{agent_id}'
                        ) subquery
                    """)
                    hcp_count = cursor.fetchone()[0]

                    # Get HCP data
                    cursor.execute(f"SELECT HCP_Name, Distance, Specialty, Preferred_Drug, Communication_Pref FROM final_assigned_hcps WHERE Agent_ID = '{agent_id}'")
                    columns = [col[0] for col in cursor.description]
                    hcp_data = [dict(zip(columns, row)) for row in cursor.fetchall()]

                    # Get chat completion data
                    cursor.execute(f"SELECT Agent_ID, response_content FROM chat_completion_dataset WHERE Agent_ID = '{agent_id}' LIMIT 1")
                    chat_data = cursor.fetchone()
                    chat_completion = chat_data[1] if chat_data else "No chat completion data available."

            return jsonify({
                'hcp_count': hcp_count,
                'hcp_data': hcp_data,
                'chat_completion': chat_completion
            })
        except Exception as e:
            print(f"Error during processing: {e}")
            return jsonify({'error': 'An error occurred while processing the request.'}), 500

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
