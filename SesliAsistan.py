from gtts import gTTS
import speech_recognition as sr
import random
import playsound
import os
import webbrowser
import datetime
import pyautogui
import tkinter as tk
import threading
import time
from random import choice
import os.path
import pyaudio
from pymata4 import pymata4
import requests
from bs4 import BeautifulSoup
import joblib
import warnings
from tkinter import simpledialog
import sys

def konuş(yazı):
    # Konuşma fonksiyonu
    tts = gTTS(text=yazı, lang="tr")
    dosya_ismi = "ses" + str(random.randint(0, 1000000000000000000000)) + ".mp3"
    tts.save(dosya_ismi)
    playsound.playsound(dosya_ismi)
    os.remove(dosya_ismi)

def mikrofonu_dinle():
    global durum_etiketi
    r = sr.Recognizer()
    konuş("Merhaba Efendim Nasıl Yardımcı Olabilirim")
    with sr.Microphone() as kaynak:
        r.energy_threshold = 1000
        dinleniyor_durumu = False
        while True:
            durum_etiketi.config(text="Dinleniyor...")
            
            try:
                if not dinleniyor_durumu:
                    ses = r.listen(kaynak, timeout=2)
                else:
                    ses = r.listen(kaynak, timeout=0.5)  # Hızlı dinleme için kısa timeout
                durum_etiketi.config(text="Tanınıyor...")
                söylenen_cümle = r.recognize_google(ses, language="tr-TR")
                durum_etiketi.config(text=f'Söylenen komut: {söylenen_cümle}\n')
                dinleniyor_durumu = False  # Komut algılandıktan sonra tekrar normal dinleme moduna geç
                if "nasılsın" in söylenen_cümle:
                    konuş("iyiyim, siz nasılsınız?")
                elif 'Google aç' in söylenen_cümle:
                    konuş("Google'ı açıyorum efendim.")
                    webbrowser.open('https://google.com')
                elif 'YouTube aç' in söylenen_cümle:
                    konuş("Youtube'u açıyorum efendim.")
                    webbrowser.open('https://www.youtube.com/')
                elif 'saat kaç' in söylenen_cümle:
                    strtime = datetime.datetime.now().strftime('%H:%M:%S')
                    konuş(f'efendim saat {strtime}')
                elif 'bilgisayar bakımı aç' in söylenen_cümle:
                    konuş('bilgisayar bakımı açıyorum efendim')
                    os.startfile("C:\BilgisayarBakım\Bilgisayar Bakım.exe")
                elif "Tarayıcıyı kapat" in söylenen_cümle:
                    konuş('tarayıcıyı kapatıyorum efendim')
                    os.system("TASKKILL /F /IM msedge.exe")
                    os.system("taskkill /f /im opera.exe")
                    os.system("taskkill /f /im chrome.exe")
                elif "çal" in söylenen_cümle:
                    kelimeler = söylenen_cümle.split(" ")
                    url = "https://www.youtube.com/results?search_query="
                    for kelime in kelimeler:
                        url = url + kelime + "+"
                    konuş('İstediğiniz şeyi çalıyorum efendim')
                    webbrowser.open_new_tab(url)
                    time.sleep(12.5)
                    pyautogui.click(934, 315, clicks=2)
                elif "seni oluşturan kim" in söylenen_cümle:
                    konuş('Beni oluşturup geliştiren kişinin ismi Emre Özcandır')
                elif "Bilgisayarı kapat" in söylenen_cümle:
                    konuş('bilgisayarınız 5 saniye içinde kapanacaktır efendim')
                    os.system("shutdown /s /t 5")
####################################################33####################################################33
                elif "not et" in söylenen_cümle:
                     r = sr.Recognizer()
                     with sr.Microphone() as source:
                       konuş("Şimdi söyleyiniz.")
                       r.pause_threshold = 2
                       audio = r.listen(source)
                      
                     try:
                       dosya = open("a.txt","a",encoding="utf-8")
                       yazı = r.recognize_google(audio, language="Tr-tr")
                       print(yazı,file=dosya)
                       dosya.close()
                       konuş('not ettim efendim')
                       
                     except sr.UnknownValueError:
                       konuş("Anlayamadım efendim. ")
####################################################33####################################################33                
                elif 'tamamdır' in söylenen_cümle:
                        konuş('tamam efendim.Görüşürüz')
                        kapat()
                        break                                              
####################################################33####################################################33

                elif 'Fıkra anlat' in söylenen_cümle:
                    fıkralar = ["Delikanlı çalıştığı şirketin mektuplarını postalayacaktı. Postacı mektuplardan birisini tartıp; 'Bu çok ağır!' dedi. 'Biraz daha pul yapıştırmamız lazım.'Delikanlı:Abi!' dedi. 'O zaman daha ağır olmaz mı?'",
                                "Temel aldığı bir daktiloyu bozuk diye geri götürdü. Satıcı;- Neresi bozuk, dün aldığında sağlamdı.Temel:İki tane 'a' yok, saat yazamıyorum.",
                                "Adam, papağanını gümrükten kolay geçirebilmek için bir kutuya koymuş, üstüne de 'kırılacak eşya' diye yazmıştı.Gümrük memuru yazıyı okuyunca, kutuyu şöyle bir silkelemeye başladı. Aynı anda içeriden papağanın bağırdığı duyuldu.'Şangur şungur.. Şangur şungur..'",
                                "Platonik aşk yaşayan adamın birinin hayalleri gerçek olur; en çok sevdiği yıldız ile karşı karşıyadır, fırsat bu fırsat derken yıldız bayana sorar: –Saçınızdan bir tutam bana verirseniz size 100 dolar veririm! Yıldız: –Hımmm 500 dolar verirsen bütün peruk senin olsun.",
                                "Bir deli hastenisnde herkes zıplıyor, Temel yerinden kımıldamıyormuş  Biz patlamış mısırız, ben tavanın altına yapışmışım.",
                                "Küçük çocuk okulun ilk günü sonunda eve döner. Annesi sorar;  Bugün okulda ne öğrendiniz? Çocuk cevaplar; Yeterli değil, yarın tekrar gitmem gerek",
                                "Karınca Ve Fil bir gün bir karınca bir file aşık olmuş. Annesi bu durumu onaylamamış  Karınca Bana değil karnımdakine acı, demiş.",
                                "Bektaşi'ye sormuşlar. Dünya öküzün boynuzlarının üstünde duruyormuş, ne diyorsun bu işe? Valla onu bilmem ama buna inanan öküzlerin olduğunu biliyorum, demiş.",
                                "Temel'in eldivenle yazı yazdığını görenler sormuş Niye eldivenli yazıyorsun zor olmuyor mu?  Zorluğuna zor ama el yazımın tanınmasını istemeyrum.",
                                "Bir toplantıda, bir genç, Mehmet Akif'i küçük düşürmek ister: - Afedersiniz, siz veteriner misiniz? Mehmet Akif hiç istifini bozmadan şöyle yanıtlamış:- Evet, bir yeriniz mi ağrıyordu?",
                                
                            
                            ]
                    secimfık=choice(fıkralar)
                    konuş(secimfık)

####################################################33####################################################33

                elif "nedir" in söylenen_cümle:
                    words = söylenen_cümle.split(" ")
                    search_query = "_".join(words[:-1]) 
                    result = wikipedia_search_and_read(search_query)
                    if result != "Sonuç bulunamadı.":
                       
                        konuş("Düşünüyorum...")
                        konuş(result)
                    else:
                        konuş("Üzgünüm, aradığınızı bulamadım.")
####################################################33####################################################33

                elif "kimdir" in söylenen_cümle:
                    words = söylenen_cümle.split(" ")
                    search_query = "_".join(words[:-1])
                    result_text = wikipedia_search_and_read(search_query)
                    
                    if result_text != "Sonuç bulunamadı.":
                        print(result_text)
                        konuş(result_text)
                    else:
                        konuş("Üzgünüm, aradığınız kişi hakkında bir şey bulamadım.")
####################################################33####################################################33
  
                elif 'arama yap' in söylenen_cümle:
                    recognizer = sr.Recognizer()

                    konuş("Aramak istediğiniz şeyi söyleyin:")
                    with sr.Microphone() as source3:
                        ses = recognizer.listen(source3)

                    try:
                        arama_metni = recognizer.recognize_google(ses, language="tr-TR")
                        konuş(f"{arama_metni} için arama yapılıyor...")
                        result = google_search(arama_metni)

                        if result != "Sonuç bulunamadı.":
                            
                            konuş('İşte bulduğum sonuç: ' + result)
                            
                            konuş(result)
                        else:
                            konuş("Üzgünüm, aradığınızı bulamadım.")

                    except sr.UnknownValueError:
                        konuş("Üzgünüm, anlayamadım. Lütfen tekrar deneyin.")
####################################################33####################################################33
           
                elif 'zararlı site tespit et' in söylenen_cümle:
                    # Uyarıları gizleme
                    warnings.filterwarnings('ignore', category=UserWarning)
                    # Modeli ve vektörleştiriciyi yükleme
                    loaded_model = joblib.load('trained_model.pkl')
                    loaded_vectorizer = joblib.load('vectorizer.pkl')

                    recognizer = sr.Recognizer()

                    konuş("Lütfen bir URL söyleyin:")
                    with sr.Microphone() as source2:
                        ses = recognizer.listen(source2)

                    try:
                        user_input = recognizer.recognize_google(ses, language="tr-TR")
                        konuş("Lütfen bekleyiniz şu anda düşünüyorum.")

                        user_input_transformed = loaded_vectorizer.transform([user_input])
                        prediction = loaded_model.predict(user_input_transformed)[0]

                        if prediction == 'good':
                            konuş("Site Sınıfı: Kötü Niyetli Değil")
                        elif prediction == 'bad':
                            konuş("Site Sınıfı: Kötü Niyetli Olabilir")
                        else:
                            konuş("Tahmin Edilemedi")
                    except sr.UnknownValueError:
                        konuş("Üzgünüm, anlayamadım. Lütfen tekrar deneyin.")
####################################################33####################################################33
                       
                elif "hastalığımı teşhis et" in söylenen_cümle:
                        from joblib import load
                        import pandas as pd
                       
                        import warnings
                        # Modeli yükle
                        loaded_model = load('hastalik_modeli.joblib')


                        # Belirli türdeki uyarıları gizlemek için filtre ayarları
                        warnings.filterwarnings("ignore", category=UserWarning)  # UserWarning'leri gizle
                        warnings.filterwarnings("ignore", category=FutureWarning)  # FutureWarning'leri gizle


                        # Sütun adları için Türkçe karşılıklarını içeren bir sözlük oluştur
                        turkish_columns = {
                            'itching': 'Kaşıntı',
                            'skin_rash': 'Cilt Döküntüsü',
                            'nodal_skin_eruptions': 'Nodüler Cilt Aşınması',
                            'continuous_sneezing': 'Sürekli Hapşırma',
                            'shivering': 'El Titremesi',
                            'chills': 'Vücudun herhangi bir yerinde Titreme',
                            'joint_pain': 'Eklem Ağrısı',
                            'stomach_pain': 'Mide Ağrısı',
                            'acidity': 'Mide Yanması',
                            'ulcers_on_tongue': 'Dilde Ülserler',
                            'muscle_wasting': 'Kas Kaybı',
                            'vomiting': 'Kusma',
                            'burning_micturition': 'Yanma İdrar Yaparken',
                            'spotting_ urination': 'İdrarda Lekeler',
                            'fatigue': 'Yorgunluk',
                            'weight_gain': 'Kilo Alımı',
                            'anxiety': 'Anksiyete',
                            'cold_hands_and_feets': 'Soğuk Eller ve Ayaklar',
                            'mood_swings': 'Mizaç Değişiklikleri',
                            'weight_loss': 'Kilo Kaybı',
                            'restlessness': 'Huzursuzluk',
                            'lethargy': 'Halsizlik',
                            'patches_in_throat': 'Boğazda Leke',
                            'irregular_sugar_level': 'Düzensiz Şeker Seviyesi',
                            'cough': 'Öksürük',
                            'high_fever': 'Yüksek Ateş',
                            'sunken_eyes': 'Çökük Gözler',
                            'breathlessness': 'Nefes Darlığı',
                            'sweating': 'Terleme',
                            'dehydration': 'Dehidrasyon',
                            'indigestion': 'Hazımsızlık',
                            'headache': 'Baş Ağrısı',
                            'yellowish_skin': 'Sarımsı Cilt',
                            'dark_urine': 'Koyu Renkli İdrar',
                            'nausea': 'Mide Bulantısı',
                            'loss_of_appetite': 'İştah Kaybı',
                            'pain_behind_the_eyes': 'Göz Arkasında Ağrı',
                            'back_pain': 'Bel Ağrısı',
                            'constipation': 'Kabızlık',
                            'abdominal_pain': 'Karın Ağrısı',
                            'diarrhoea': 'İshal',
                            'mild_fever': 'Hafif Ateş',
                            'yellow_urine': 'Sarı İdrar',
                            'yellowing_of_eyes': 'Gözlerin Sararması',
                            'acute_liver_failure': 'Akut Karaciğer Yetmezliği',
                            'fluid_overload': 'Sıvı Fazlalığı',
                            'swelling_of_stomach': 'Karın Şişmesi',
                            'swelled_lymph_nodes': 'Şişmiş Lenf Noktaları',
                            'malaise': 'Halsizlik',
                            'blurred_and_distorted_vision': 'Bulanık ve Bozulmuş Görme',
                            'phlegm': 'Balgam',
                            'throat_irritation': 'Boğaz İrritasyonu',
                            'redness_of_eyes': 'Gözlerde Kızarıklık',
                            'sinus_pressure': 'Sinüs Basıncı',
                            'runny_nose': 'Burun Akması',
                            'congestion': 'Tıkanıklık',
                            'chest_pain': 'Göğüs Ağrısı',
                            'weakness_in_limbs': 'Eklem Güçsüzlüğü',
                            'fast_heart_rate': 'Hızlı Kalp Atışı',
                            'pain_during_bowel_movements': 'Bağırsak Hareketleri Sırasında Ağrı',
                            'pain_in_anal_region': 'Anal Bölgede Ağrı',
                            'bloody_stool': 'Kanlı Dışkı',
                            'irritation_in_anus': 'Anal Bölgede İrritasyon',
                            'neck_pain': 'Boyun Ağrısı',
                            'dizziness': 'Baş Dönmesi',
                            'cramps': 'Kramplar',
                            'bruising': 'Morarma',
                            'obesity': 'Obezite',
                            'swollen_legs': 'Şişmiş Bacaklar',
                            'swollen_blood_vessels': 'Şişmiş Kan Damarları',
                            'puffy_face_and_eyes': 'Şişmiş Yüz ve Gözler',
                            'enlarged_thyroid': 'Büyümüş Tiroid',
                            'brittle_nails': 'Kırılgan Tırnaklar',
                            'swollen_extremeties': 'Şişmiş Parmak Uçları',
                            'excessive_hunger': 'Aşırı Açlık',
                            'extra_marital_contacts': 'Ekstra Evlilik Dışı İlişkiler',
                            'drying_and_tingling_lips': 'Kuruma ve Karıncalanan Dudaklar',
                            'slurred_speech': 'Geveleyerek Konuşma',
                            'knee_pain': 'Diz Ağrısı',
                            'hip_joint_pain': 'Kalça Eklem Ağrısı',
                            'muscle_weakness': 'Kas Zayıflığı',
                            'stiff_neck': 'Sert Boyun',
                            'swelling_joints': 'Şişmiş Eklem',
                            'movement_stiffness': 'Hareket Sertliği',
                            'spinning_movements': 'Dönme Hareketleri',
                            'loss_of_balance': 'Denge Kaybı',
                            'unsteadiness': 'Kararsızlık',
                            'weakness_of_one_body_side': 'Bir Vücut Tarafının Zayıflığı',
                            'loss_of_smell': 'Koku Kaybı',
                            'bladder_discomfort': 'Mesane Rahatsızlığı',
                            'foul_smell_of urine': 'İdrarın Kötü Kokusu',
                            'continuous_feel_of_urine': 'Sürekli İdrar Hissi',
                            'passage_of_gases': 'Gaz Geçişi',
                            'internal_itching': 'İç Kaşıntı',
                            'toxic_look_(typhos)': 'Toksik Görünüm (tifüs)',
                            'depression': 'Depresyon',
                            'irritability': 'Sinirlilik',
                            'muscle_pain': 'Kas Ağrısı',
                            'altered_sensorium': 'Değişmiş Algı',
                            'red_spots_over_body': 'Vücutta Kırmızı Noktalar',
                            'belly_pain': 'Karın Ağrısı',
                            'abnormal_menstruation': 'Anormal Adet Dönemi',
                            'dischromic _patches': 'Renk Değişimi',
                            'watering_from_eyes': 'Gözlerden Su Gelmesi',
                            'increased_appetite': 'Artan İştah',
                            'polyuria': 'Polüüri',
                            'family_history': 'Aile Geçmişi',
                            'mucoid_sputum': 'Mukoit Balgam',
                            'rusty_sputum': 'Paslı Balgam',
                            'lack_of_concentration': 'Dikkat Eksikliği',
                            'visual_disturbances': 'Görsel Bozukluklar',
                            'receiving_blood_transfusion': 'Kan Transfüzyonu ',
                            'receiving_unsterile_injections': 'Steril Olmayan Enjeksiyon ',
                            'coma': 'Koma',
                            'stomach_bleeding': 'Mide Kanaması',
                            'distention_of_abdomen': 'Karında Genişleme',
                            'history_of_alcohol_consumption': 'Alkol Tüketim Geçmişi',
                            'blood_in_sputum': 'Balgamda Kan',
                            'prominent_veins_on_calf': 'Baldırda Belirgin Damarlar',
                            'palpitations': 'Çarpıntılar',
                            'painful_walking': 'Acılı Yürüme',
                            'pus_filled_pimples': 'Apseye Dönüşmüş Sivilceler',
                            'blackheads': 'Siğiller',
                            'scurring': 'Pullanma',
                            'skin_peeling': 'Cilt Dökülmesi',
                            'silver_like_dusting': 'Gümüş Toz Gibi Siğiller',
                            'small_dents_in_nails': 'Tırnaklarda Küçük Çukurlar',
                            'inflammatory_nails': 'Enflamatuar Tırnaklar',
                            'blister': 'Kabarcık',
                            'red_sore_around_nose': 'Burun Etrafında Kırmızı Yara',
                            'yellow_crust_ooze': 'Sarı Kabuk Akıntısı',
                            'prognosis': 'Daha önce herhangi bir Teşhis'
                        }
                        
                        def recognize_speech(timeout=3):
                            recognizer = sr.Recognizer()  # recognizer değişkenini fonksiyon içinde tanımla
                            with sr.Microphone() as source3:
                                recognizer.adjust_for_ambient_noise(source3)
                                try:
                                    konuş("Konuşun...")
                                    audio = recognizer.listen(source3, timeout=timeout)
                                    text = recognizer.recognize_google(audio, language='tr-TR')
                                    return text.lower()
                                except sr.WaitTimeoutError:
                                    konuş("Zaman aşımı! Lütfen daha hızlı cevap verin.")
                                    return ""
                                except sr.UnknownValueError:
                                    konuş("Anlaşılamadı! Lütfen tekrar deneyin.")
                                    return ""
                                except sr.RequestError:
                                    konuş("Sistem hatası! Lütfen tekrar deneyin.")
                                    return ""


                        # Belirtileri sormak için döngü
                        symptoms = []

                        for symptom_key, symptom_value in turkish_columns.items():
                            while True:
                                konuş(f"{symptom_value} var mı?")
                                answer = recognize_speech(timeout=3)  # 3 saniye içinde cevap beklenir
                                mesaj2 = f"Algılanan cevap: {answer}"  # Kullanıcının verdiği cevabı yazdır
                                durum_etiketi.config(text=mesaj2)

                                if answer == 'evet' or answer == 'hayır':
                                    break  # Geçerli bir cevap alındı, döngüden çık
                                else:
                                    konuş("Lütfen 'evet' veya 'hayır' olarak cevap verin.")

                            if answer == 'evet':
                                symptoms.append('E')
                            else:
                                symptoms.append('H')
                        # Kullanıcının girdiği belirtileri modele uygun formatta düzenleme
                        user_input = pd.DataFrame([symptoms], columns=turkish_columns.keys())

                        # Semptomları modelin anlayabileceği formata dönüştürme
                        for col in user_input.columns:
                            if user_input[col][0] == 'E':
                                user_input[col] = 1
                            else:
                                user_input[col] = 0

                        # Tahmin yapma
                        predicted_disease = loaded_model.predict(user_input)

                        konuş(f"Tahmin edilen hastalık: {predicted_disease[0]}")
                  
####################################################33####################################################33
                 
                elif söylenen_cümle != "":
                        article_title = söylenen_cümle  
                        article = wikihow_search(article_title)
                        if article:
                            konuş('Düşünüyorum...')
                            parçalı_okuma(article)
                        else:
                            konuş("Söylediğiniz şey hakkında malesef bir fikrim yok.")  
####################################################33####################################################33
                            
           
            
            except Exception as e:
                hatamesaji = "Hata: {0}".format(e)
                durum_etiketi.config(text=hatamesaji)
                # Hata kaydı için dosyaya yazma
                with open("hata_logu.txt", "a") as dosya:
                    dosya.write(hatamesaji + "\n")
            
            finally:
                durum_etiketi.config(text="Beklemede...")
####################################################33####################################################33             
def kapat():
    os.system("taskkill /f /im python3.10.exe")
    root.destroy()
####################################################33####################################################33
    
def baslat():
    threading.Thread(target=mikrofonu_dinle).start()
####################################################33####################################################33
    
def wikipedia_search_and_read(query):
    url = f"https://tr.wikipedia.org/wiki/{query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    search_result = soup.find('div', {'class': 'mw-parser-output'})

    if search_result:
        paragraphs = search_result.find_all('p')
        result_text = ' '.join([para.text for para in paragraphs[:2]])  
        return result_text
    else:
        return "Sonuç bulunamadı."
####################################################33####################################################33
def google_search(query):
    url = f"https://www.google.com/search?q={query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    search_results = soup.find_all("div", class_="BNeawe s3v9rd AP7Wnd")

    if search_results:
        result_text = search_results[0].get_text()
        return result_text
    else:
        return "Sonuç bulunamadı."
####################################################33####################################################33
        
def wikihow_search(query):
    url = f"https://www.wikihow.com.tr/{query.replace(' ', '-')}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    article = soup.find('div', {'class': 'content'})

    return article
####################################################33####################################################33

def parçalı_okuma(article):
    steps = article.find_all('div', {'class': 'step'})
    if steps:
        for step in steps:
            step_text = step.get_text(separator='\n')
            konuş(step_text)
            time.sleep(2)  # Her adım arasında 2 saniye bekleyin
    else:
        konuş("Söylediğiniz konu hakkında bir fikrim ve bilgim malesef yok. Başka türlü sormayı deneyin.")
####################################################33####################################################33
        
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Sesli Asistan")
    durum_etiketi = tk.Label(root, text="Merhaba Hoşgeldiniz..")
    durum_etiketi.pack(padx=10, pady=10)
    baslat()  # Program başladığında dinleme işlevini otomatik başlatır
    button = tk.Button(root, text="Kapat", command=kapat)
    button.pack()
    root.mainloop()

