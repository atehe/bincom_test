"""Python script to create html page for query result (of questions in bincom interview test)"""


from config_db import create_db_connection, execute_query, read_query


def create_html_page(connection, query, html_page):
    query_result = read_query(connection, query)

    with open(html_page, "w") as page:
        page.write("<style>table, th, td {border:1px solid black;}</style>")
        page.write("<body><table>\n")

        # create <tr>  element for each row in query result
        for num, row_data in enumerate(query_result):
            page.write("<tr>\n")

            # create columns for each data in row
            for col in row_data:
                if num == 0:
                    page.write(f"<th>{col}</th>\n")
                else:
                    page.write(f"<td>{col}</td>\n")

            page.write("</tr>\n")
        page.write("</table></body>")
        print(f"{html_page} Created")


QUERY_1 = """
SELECT p.polling_unit_name, a.* 
FROM announced_pu_results a
JOIN polling_unit p 
ON a.polling_unit_uniqueid = p.uniqueid
WHERE a.polling_unit_uniqueid = 9;
"""

QUERY_2 = """
SELECT l.lga_name,p.polling_unit_name, SUM(a.party_score) summed_total
FROM lga l
JOIN polling_unit p
ON l.lga_id = p.lga_id
JOIN announced_pu_results a
ON a.polling_unit_uniqueid = p.uniqueid
WHERE l.lga_id = 35
GROUP BY 1,2;
"""

PASSWORD = "root"
db_connection = create_db_connection("localhost", "root", PASSWORD, "bincom_test")

create_html_page(db_connection, QUERY_1, "solutions/solution_1.html")
create_html_page(db_connection, QUERY_2, "solutions/solution_2.html")
