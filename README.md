# 🧾 Tax169 Automation  

**Automated Quarterly Tax Report Submission for Iran’s Tax Organization (سامانه 169)**  

## 📌 Overview  
**Tax169 Automation** is a Python-based automation tool built with **Selenium WebDriver** that simplifies the process of submitting quarterly tax reports to Iran’s official tax portal (**سامانه 169**).  
It logs into the system automatically, fills out required forms, uploads Excel data, and submits the final report — all without manual intervention.  

## ⚙️ Features  
- ✅ **Automated Login** — securely logs into the 169 portal using stored credentials  
- ✅ **Excel Integration** — reads taxpayer data, goods, and services directly from Excel sheets  
- ✅ **Smart Form Filling** — automatically fills and validates required tax fields  
- ✅ **Headless Mode Support** — runs silently without showing a browser window  
- ✅ **Error Handling & Logging** — detects submission errors and logs them  
- ✅ **Session Handling** — maintains active sessions and retries automatically  

## 🧰 Technologies Used  
- **Python 3.x**  
- **Selenium WebDriver**  
- **Pandas**  
- **ChromeDriver / GeckoDriver**  
- **dotenv**  

## 🚀 How It Works  
1. Provide your Excel files containing sales/purchase tax data.  
2. The script launches the [Tax Portal (169)](https://tax.gov.ir/169) using Selenium.  
3. It logs in using your credentials (from `.env` file).  
4. Uploads and fills data rows automatically.  
5. Submits the report and logs the submission status.  


## ⚠️ Notes  
- This project is intended **for educational and internal use only**.  
- It **does not bypass** authentication or captcha mechanisms.  
- Users are responsible for complying with Iranian tax regulations when using automation tools.  

---

👨‍💻 Developed by [Ehsan Samiei](https://github.com/Ehsansamiei)


