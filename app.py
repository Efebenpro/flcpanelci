from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')
    
@app.route('/anasayfa')
def index():
    return render_template('anasayfa.html')

@app.route('/adsoyad')
def adsoyad():
    return render_template('adsoyad.html')

@app.route('/tc')
def tc():
    return render_template('tc.html')

@app.route('/gsm')
def gsm():
    return render_template('gsm.html')

@app.route('/tcgsm')
def tcgsm():
    return render_template('gsm.html')

@app.route('/aile')
def aile():
    return render_template('aile.html')
  
@app.route('/sulale')
def sulale():
    return render_template('sulale.html')

@app.route('/iban')
def iban():
    return render_template('iban.html')

@app.route('/smsbomber')
def smsbomber():
    return render_template('smsbomber.html')

@app.route('/eczane')
def eczane():
    return render_template('eczane.html')    

@app.route('/mevzun')
def mevzun():
    return render_template('mevzun.html')

@app.route('/plaka')
def plaka():
    return render_template('plaka.html')
  
@app.route('/adres')
def adres():
    return render_template('adres.html')
  
@app.route('/sorgula', methods=['POST'])
def sorgula():
    ad = request.form['ad']
    soyad = request.form['soyad']
    il = request.form.get('il', '')
    ilce = request.form.get('ilce', '')

    if il and ilce:
        api_url = f"https://srgla-api.glitch.me/adsoyad.php?ad={ad}&soyad={soyad}&il={il}&ilce={ilce}"
    elif il:
        api_url = f"https://srgla-api.glitch.me/adsoyad.php?ad={ad}&soyad={soyad}&il={il}"
    else:
        api_url = f"https://srgla-api.glitch.me/adsoyad.php?ad={ad}&soyad={soyad}"

    response = requests.get(api_url)
    data = response.json()
    results = data.get('veri', [])
    return render_template('adsoyad.html', results=results)

@app.route('/tc_sorgula', methods=['POST'])
def tc_sorgula():
    tc = request.form['tc']
    api_url = f"https://srgla-api.glitch.me/tcpro.php?tc={tc}"
    response = requests.get(api_url)
    data = response.json()
    results = data.get('veri', [])
    return render_template('tc.html', results=results)
  
@app.route('/gsm', methods=['POST'])
def gsm_sorgula():
    tc = request.form['tc']
    api_url = f"https://srgla-api.glitch.me/gsm.php?gsm={tc}"
    response = requests.get(api_url)
    data = response.json()
    results = data.get('veri', [])
    return render_template('gsm.html', results=results)

@app.route('/tcgsm_sorgula', methods=['POST'])
def tcgsm_sorgula():
    tc = request.form['tc']
    api_url = f"https://srgla-api.glitch.me/gsm.php?gsm={tc}"
    response = requests.get(api_url)
    data = response.json()
    results = data.get('veri', [])
    return render_template('tcgsm.html', results=results)

@app.route('/aile_sorgula', methods=['POST'])
def aile_sorgula():
    tc = request.form['tc']
    api_url = f"https://srgla-api.glitch.me/aile.php?tc={tc}"
    response = requests.get(api_url)
    data = response.json()
    results = data.get('veri', [])
    return render_template('aile.html', results=results)

@app.route('/sulale_sorgula', methods=['POST'])
def sulale_sorgula():
    tc = request.form['tc']
    api_url = f"https://srgla-api.glitch.me/sulale.php?tc={tc}"
    response = requests.get(api_url)
    data = response.json()
    results = data.get('veri', [])
    return render_template('sulale.html', results=results)
  
@app.route('/adres_sorgula', methods=['POST'])
def adres_sorgula():
    tc = request.form['tc']
    api_url = f"https://srgla-api.glitch.me/adres.php?tc={tc}"
    response = requests.get(api_url)
    data = response.json()
    return render_template('adres.html', results=data)

@app.route('/mevzun_sorgula', methods=['POST'])
def mevzun_sorgula():
    tc = request.form['tc']
    api_url = f"https://srgla-api.glitch.me/mevzun.php?tc={tc}"
    response = requests.get(api_url)
    data = response.json()
    return render_template('adres.html', results=data)

@app.route('/eczane_sorgula', methods=['POST'])
def eczane_sorgula():
    tc = request.form['tc']
    api_url = f"https://srgla-api.glitch.me/eczane.php?ad={tc}"
    response = requests.get(api_url)
    data = response.json()
    return render_template('eczane.html', results=data)

@app.route('/plaka_sorgula', methods=['POST'])
def plaka_sorgula():
    tc = request.form['tc']
    api_url = f"https://srgla-api.glitch.me/plaka?plaka={tc}"
    response = requests.get(api_url)
    data = response.json()
    return render_template('plaka.html', results=data)


if __name__ == '__main__':
    app.run(debug=True)

