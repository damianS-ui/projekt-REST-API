from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

NASA_IMAGE_API_URL = "https://images-api.nasa.gov/search"

@app.route("/nasa/images", methods=["GET"])
def get_nasa_images():
    query = request.args.get("q", "mars")  # domyślnie 'mars' jeśli brak parametru
    try:
        response = requests.get(
            NASA_IMAGE_API_URL,
            params={"q": query, "media_type": "image"},
            timeout=10
        )
        response.raise_for_status()
        data = response.json()

        items = []
        for item in data.get("collection", {}).get("items", []):
            links = item.get("links", [])
            if links:
                image_url = links[0].get("href")
                title = item.get("data", [{}])[0].get("title")
                items.append({"title": title, "url": image_url})

        return jsonify({"query": query, "results": items})

    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Request failed: {e}"}), 500


# zwraca zdjecia
@app.route("/nasa/images_html", methods=["GET"])
def get_nasa_images_html():
    query = request.args.get("q", "mars")
    try:
        response = requests.get(
            NASA_IMAGE_API_URL,
            params={"q": query, "media_type": "image"},
            timeout=10
        )
        response.raise_for_status()
        data = response.json()

        items = []
        for item in data.get("collection", {}).get("items", []):
            links = item.get("links", [])
            if links:
                image_url = links[0].get("href")
                title = item.get("data", [{}])[0].get("title")
                items.append((title, image_url))

        # HTML z miniaturkami
        html = f"<h1>NASA Images for '{query}'</h1>"
        html += "<div style='display: flex; flex-wrap: wrap;'>"
        for title, url in items:
            html += f"""
            <div style='margin:10px; text-align:center;'>
                <h4 style='width:300px'>{title}</h4>
                <img src='{url}' width='300'>
            </div>
            """
        html += "</div>"
        return html

    except requests.exceptions.RequestException as e:
        return f"Error: {e}", 500


if __name__ == "__main__":
    app.run(port=8001, debug=True)
