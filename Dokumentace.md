# **Auto Evaluátor – Predikce ceny a výhodnosti ojetých vozů**

---

## **Autor**
**Ondřej Novotný**  
Email: ondra.novotny.2006@gmail.com  

---

## **Popis aplikace**
Auto Evaluátor je desktopová aplikace vytvořená v Pythonu, která umožňuje:

- **Predikovat reálnou tržní cenu** ojetého vozu na základě jeho parametrů
- **Zhodnotit výhodnost nabídky** pomocí klasifikace (`Deal Score`)
- **Volitelně nechat cenu automaticky doplnit podle predikce**

Aplikace využívá architekturu **Model - View - Controller (MVC)** a je navržena jako uživatelsky přívětivá, s jednoduchým GUI v knihovně Tkinter.

---

## **Funkcionalita**
-  Predikce ceny pomocí **RandomForestRegressoru**
-  Klasifikace nabídky na "Výhodná / Průměrná / Nevýhodná" pomocí **neuronové sítě**
-  Možnost **ručně zadat cenu** nebo ji **automaticky predikovat**
-  Zpracování vstupních dat pomocí TargetEncoderu a StandardScaleru

---

## **Způsob spuštění**
### 1. Stáhnutí projektu
Stáhni nebo rozbal složku projektu

### 2. Přesun do složky `src`
```bash
cd cesta/k/projektu/src
```

### 3. Instalace potřebných knihoven
Nainstalovat ručně:


```bash
pip install pandas 
```
```bash
pip install numpy 
```
```bash
pip install scikit-learn 
```
```bash
pip install tensorflow 
```
```bash
pip install category_encoders
```
```bash
pip install  joblib
```
### 4. Spuštění aplikace
```bash
python main.py
```
Alternativně:
```bash
python C/cesta/k/souboru/main.py
```

---

## **Struktura projektu**

```
car_app/
├── controller.py       
├── model.py          
├── view.py             
├── main.py             
├── price_model.pkl     
├── deal_model.h5      
├── deal_encoder.pkl    
├── deal_scaler.pkl     
└── README.md           
```

---

## **Použité technologie**

| Nástroj / Knihovna | Použití |
|--------------------|---------|
| `scikit-learn`     | RandomForestRegressor pro predikci ceny |
| `tensorflow`       | Keras Sequential model pro klasifikaci |
| `category_encoders`| TargetEncoder pro kódování kategorií |
| `Tkinter`          | GUI rozhraní |
| `pandas` / `numpy` | Práce s daty |
| `joblib`           | Ukládání / načítání modelů |

---

## **Architektura MVC**

| Soubor | Role |
|--------|------|
| **Model** | Načítání modelů, predikce, preprocessing |
| **View**  | Uživatelské rozhraní pro zadání vstupních dat |
| **Controller** | Řídí logiku, propojuje model a GUI |

---

## **Vstupní parametry vozidla**

- Značka (např. Škoda)
- Model (např. Octavia)
- Rok první registrace
- Výkon (v kW)
- Spotřeba (v L/100km)
- Najeto (v km)
- Cena (volitelná — může být predikována)

---

## **Způsob predikce a klasifikace**
###  Predikce ceny
- Algoritmus: `RandomForestRegressor`
- Inputy: Značka, Model, Rok, Výkon, Spotřeba, Najeto
- Výstup: Reálná tržní cena vozidla

###  Klasifikace výhodnosti
- Algoritmus: Vícevrstvá neuronová síť (`Keras`)
- Třídy: Výhodná (1), Průměrná (2), Nevýhodná (3)
- Inputy: Všechny výše zmíněné + Cena

---

## **Zdroje**
Zdroje, které byly použity pouze jako inspirace a částečné reference:
- Aktivační funkce neuronových sítí: https://www.datacamp.com/tutorial/introduction-to-activation-functions-in-neural-networks
- XGBoost info (nepoužito ve finálním projektu): https://www.ibm.com/think/topics/xgboost
- Základy : https://pythongeeks.org/artificial-neural-network/

---
## **Průběh trénování modelů**

Průběh čištení, sběru dat a  trénování, výběr modelů jsou zde:

- Creawler na sběr dat:

(https://github.com/novotny13/Crawler)


---
- Google colab notebook:

(https://colab.research.google.com/drive/17gVRENaFeU7SHlMODoJfrBQZ7u1BfTT4?usp=sharing)


###  Použité data sety jsou ve složce `data` v zipu projektu

---
## **Poznámky k použití**
- Modely jsou již natrénovány a uložené (`.pkl`, `.h5`)
- V případě potřeby lze modely znovu trénovat zde (https://colab.research.google.com/drive/1bcM1LQRyVJcsX6Bij9yywkuhhjJSdEOJ?usp=sharing)
- Aplikace je plně offline

---

## **Závěr**
Projekt Auto Evaluátor je jednoduchý nástroj s praktickým využitím, který kombinuje tradiční ML a hluboké učení. Umožňuje uživateli rychle zjistit, zda je nabídka vozidla výhodná, a zároveň odhadnout jeho reálnou cenu.

---

**© 2025 Ondřej Novotný**