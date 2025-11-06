# projekt-REST-API

Ten projekt udostępnia mikroserwisy do pobierania danych i obrazów z NASA.

---

## Wymagania

Pobierz zależności z pliku `requirements.txt`:

```bash
pip install -r requirements.txt


przejdz do projektu w terminalu 
cd system-nasa-rest-api\service-nasa

uruchom server
python app.py

POSTMAN http://127.0.0.1:8001/nasa/images?q=apollo

W Przeglądarce: http://127.0.0.1:8001/nasa/images_html?q=<fraza do wyszukania>



