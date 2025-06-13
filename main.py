from flask import Flask, request, render_template_string
import datetime
import requests

app = Flask(__name__)

GOOGLE_SHEET_WEBHOOK_URL = "https://script.google.com/macros/s/AKfycbzdmmiEFnSuGHI8hZtgxS-LlNjb8UdhpVPoEng3TO4xQJuity0vIAZpJ2nBnv3iagxq/exec"


@app.route("/track")
def track():
    option = request.args.get("option", "")
    msg = request.args.get("msg", "")
    ip = request.remote_addr
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    payload = {
        "timestamp": timestamp,
        "ip": ip,
        "option": option,
        "custom_msg": msg
    }
    try:
        requests.post(GOOGLE_SHEET_WEBHOOK_URL, data=payload)
    except Exception as e:
        print("Failed to track:", e)
    return "", 204


@app.route("/", methods=["GET", "POST"])
def secret():
    if request.method == "POST":
        option = request.form.get("option", "")
        custom_msg = request.form.get("custom_msg", "")
        device_ip = request.remote_addr
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        payload = {
            "timestamp": timestamp,
            "ip": device_ip,
            "option": option + " (Submitted)",
            "custom_msg": custom_msg
        }
        try:
            requests.post(GOOGLE_SHEET_WEBHOOK_URL, data=payload)
        except Exception as e:
            print("Failed to send to Google Sheets:", e)

    return render_template_string("""<!DOCTYPE html>
<html>
<head>
    <title>Secret Message</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            font-family: 'Segoe UI', sans-serif;
            background: #f1f9ff;
            padding: 20px;
            line-height: 1.6;
        }
        .container {
            background: white;
            padding: 25px;
            border-radius: 12px;
            box-shadow: 0 0 12px rgba(0,0,0,0.1);
            max-width: 850px;
            margin: auto;
        }
        h2 {
            text-align: center;
            color: #084c61;
        }
        .section {
            margin: 20px 0;
        }
        .highlight {
            background: #ffe5e5;
            padding: 10px;
            border-left: 4px solid red;
            margin-bottom: 10px;
        }
        .option {
            background: #eef6ff;
            border: 2px solid #084c61;
            border-radius: 8px;
            padding: 15px;
            margin-bottom: 30px;
            font-weight: bold;
            cursor: pointer;
        }
        .option:hover {
            background: #d8f0ff;
        }
        textarea {
            width: 100%;
            height: 100px;
            border-radius: 8px;
            padding: 10px;
            font-size: 15px;
            border: 1px solid #ccc;
        }
        .submit-btn {
            background: #28a745;
            color: white;
            border: none;
            padding: 12px 20px;
            border-radius: 8px;
            font-size: 17px;
            cursor: pointer;
            display: block;
            margin: 20px auto;
        }
        @media screen and (max-width: 600px) {
            body {
                padding: 10px;
            }
            .option {
                font-size: 16px;
            }
        }
    </style>
    <script>
        function trackOption(val) {
            fetch("/track?option=Option " + val);
        }
        let typingTimer;
        function trackMessage(val) {
            clearTimeout(typingTimer);
            typingTimer = setTimeout(() => {
                fetch("/track?msg=" + encodeURIComponent(val));
            }, 1500);
        }
    </script>
</head>
<body>
<div class="container">
    <h2>📜 A Secret Just For You</h2>
    <div class="section highlight">
        <strong>Apko bacho ki kasam hai</strong><br>
        Ye message agar ho sakey toh sirf apke aur mere beech rahey.<br>
        ye apne bache aur unki life aur future ke liye bohot zruri hai .
    </div>
    <div class="section">
        Tumse sirf itna kehna tha...<br><br>
        Ke Bhot waqt laga diya tumne faisla lene me,ye faisla agar tum
        pehle le lete toh kya hi bigad jata <br>
        Lekin finally shayd ab lagta hai Allah ne finally tumhe is qabil bana diya hai ke <strong>tum as a maa hi sahi par apne bacho ke liye jo himmat dikhayi hai woh izzat karne layak hai aur ab bacho ka faisla tum khud le sakti ho aur tumhare liye ye itna asan nahi raha hoga me ye janta hu  </strong>.<br><br>
      Ab baat jab tumhre bacho ki hai toh please isme Kisi aur ki advice mt lena khud hi decision lena chahe aaj ho ya hamesha — <strong> kyunki wo zamane ke liye bojh ho saktey tumhare aur mere liye nahi aur jo tum soch aur kar sakti ho apne bacho ke liye, wo koi aur nahi soch sakta aur na kar sakta</strong><br><br>
        Agar phir bhi zarurat mehsoos ho, toh <strong>sirf Allah se istekhara</strong> kar lena.
    </div>
    <div class="section">
        Beshaq ab shyad tumhare aur meere beech kuch nahi bacha h par 3 bache h jinhe bachana bhot zruri hai har haal mein Agar tumne Allah ko hazir nazir jaankar bacho ke liye soch rahi ho <strong> Toh ye koi film nahi h ke phir se shuru ho jaayegi jo waqt guzarta jayega wo wapas nahi ayega jab bache barbaad ho jayenge  toh aap aur hum waqt me wapas nahi ja payenge sab sahi karne ko </strong>,<br>

        toh <strong> Ab Jo himmat tumne bacho ke liye dikhayi hai wo izzat karne layak h  </strong>. ❤️<br>

        <strong> But Unke liye thodi aur samjh bhi dikhao agar aap ne aur mene dono ne milkar bacho ko safe nahi kara toh hum unhe humesha ke liye barbaad kar denge.
        </strong>
         <strong> Filhaal shayad abhi apne pass kuch options hai toh Tum in options me se ek faisla le lo jo bhi faisla logi main inshallah tumhare liye wo hi 100 percent krne ki koshish karunga apne bacho ke khatir .</strong>
    </div>
    <form method="POST">
        <div class="option" onclick="document.getElementById('option1').checked = true; trackOption(1);">
            <input type="radio" name="option" value="1" id="option1">
            <label for="option1"><strong>1️⃣ Pehla: Tum agar chahte ho ke tumhe sirf bache mil jaaye aur uske baad bacho ko aur tumhe meri zarurat nahi hai toh phir mein apse waada karta tumhe aur bacho ko kabhi nahi milunga. Ye waada raha. Tumhe bache aur jo chaiye wo tmhe mil jayega bina mere interaction phir unki life par akele poora tumhara control hoga unke ache aur burey ke liye tum poori trah responsible hoge . Toh is option ko chuno aur aur apna jawab submit karo.</strong></label>
        </div>
        <div class="option" onclick="document.getElementById('option2').checked = true; trackOption(2);">
            <input type="radio" name="option" value="2" id="option2">
            <label for="option2"><strong>2️⃣ Agar tumhe lagta hai ke apne bacho ko acha future aur ek khubsurat bachpan, unhe top most education, strong confident mindset, unki bachpan ki khwaishey aur shauq, ek izzat wali zindagi jisme kisi ke taaney na ho, bachiyo ki izzat aur izzatdar ghro me unki shaadi aur wo har cheez jin par unka haq hai aur allah karey duniya ki har khushi unhe miley — in sabke liye aur apan dono ko milkar sirf bacho ke liye apna 100% dekar unke future ke liye apan ko koi aisa alternative raasta nikalna hoga jisse ye sab possible ho — toh is option ko chuno..</strong> (Agar tum ye option chunoge toh me next secret status msg me discuss karunga ke apan kya kya kr saktey h)</label>
        </div>
        <div class="option" onclick="document.getElementById('option3').checked = true; trackOption(3);">
            <input type="radio" name="option" value="3" id="option3">
            <label for="option3"><strong>3️⃣ Aur agar sirf apan ko poori zindagi tamasha hi karna hai aur uski kimat apne bacho ko barbaad karke chukana , wo bhi na jaaney kis baat ke liye — jo na tumhe sahi se pata h aur na mujhe — aur bas aise kisi masley le apne aur hmne apni haadein paar kar li aur apne beech sab barbad kr liya, aur ab bacho ko bhi barbaad kr rahey, unka future, unki life, everything — toh agar tmhe ye option chunna h toh chunne ki zrurat nahi, kyunki mubarak ho abhi apan al ready usi raastey pe h.</strong></label>
        </div>
        <strong>Ya agar tum kuch aur kehna chahti ho:</strong><br>
        <textarea name="custom_msg" placeholder="Yahan likho jo tumhare dil mein ho..." oninput="trackMessage(this.value)"></textarea>
        <button class="submit-btn" type="submit">✅ Bhot soch kar sahi option chun kar hi ye button dabana  </button>
    </form>
</div>
</body>
</html>""")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)
