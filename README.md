# 🏦 Xeria Bank Assistant Bot

### Rasa NLU Powered Banking Support Assistant

![Xeria Bank Assistant Bot](xeria-bank-assistant_bot.png)

> A banking support chatbot built using **Rasa Open Source NLU** and **Streamlit**, designed to understand customer intent, classify banking queries, and provide instant assistance through a conversational interface.

---

# 📖 Project Story

Most beginner chatbots rely on simple **if-else statements** and keyword matching.

This project originally started the same way.

The first version of Xeria Bank Assistant was a rule-based chatbot built in Streamlit. While it could answer basic banking questions, it had major limitations:

❌ Failed when users used different wording

❌ Could not handle spelling mistakes

❌ Required hardcoded conditions for every query

❌ Became difficult to maintain as services increased

For example:

```text
check balance
```

might work, but:

```text
can you tell me how much money is left in my account?
```

would often fail.

To solve this problem, the chatbot was redesigned using **Rasa Open Source NLU**.

Instead of searching for keywords, the assistant now understands the **intent behind a customer's message**, making conversations far more natural and scalable.

---

# 🚀 Final Solution

Xeria Bank Assistant is a fully local banking chatbot powered by:

* Rasa Open Source 3.6.21
* Streamlit
* Python 3.10.11

The assistant uses Natural Language Understanding (NLU) to:

* Identify customer intent
* Predict confidence scores
* Route conversations correctly
* Handle banking service requests
* Escalate users to human support when required

The project runs completely offline and does not use:

* OpenAI APIs
* Gemini APIs
* LangChain
* Vector Databases
* External AI Services

---

# 📸 Project Walkthrough

## 🏦 Main Application Dashboard

The main interface displays the banking assistant, quick service shortcuts, session information, and Rasa server status.

![Main Dashboard](xeria-bank-assistant_bot.png)

---

## 👋 Greeting Intent Recognition

The assistant successfully detects greeting intents and responds appropriately.

![Greeting Intent](Greeting.png)

---

## 🏠 Banking Product Query

Customers can ask about banking products such as home loans and receive relevant responses.

![Banking Query](Banking%20Query.png)

---

## 🎯 Intent Classification & Confidence Score

One of the biggest improvements over the original chatbot is the ability to predict user intent with confidence scores.

![Confidence Score](Confidence%20Score.png)

---

## 💬 Casual Conversation Support

The assistant can understand conversational phrases such as:

* Thanks
* Yes
* No
* Repeat
* Clarification Requests

![Casual Conversation](Casual%20Conversation.png)

---

## 🧑‍💼 Human Support Escalation

When the chatbot cannot fully resolve an issue, it escalates the user to customer support.

![Human Escalation](Human%20Escalation.png)

---

## 🧠 Rasa Model Training

The chatbot model was trained locally using Rasa Open Source.

![Rasa Training](rasa_training.png)

---

## 🚀 Rasa Server Deployment

The trained model is loaded into a Rasa server and exposed through REST APIs consumed by the Streamlit frontend.

![Rasa Server](rasa_server.png)

---

# ✨ Key Features

### Natural Language Understanding

* Intent Classification
* Confidence Prediction
* Fallback Handling
* Conversation Flow Management

### Banking Services

* Account Opening
* Savings Account
* Current Account
* Balance Enquiry
* Account Statement

### Card Services

* Debit Card
* Credit Card
* Card Blocking
* Lost Card Reporting
* PIN Reset

### Loan Services

* Personal Loan
* Home Loan
* Loan Information

### Additional Services

* Fixed Deposit Information
* Branch Locator
* Complaint Registration
* Net Banking Support
* Human Agent Escalation

### User Experience

* Modern Banking UI
* Chat History
* Quick Service Buttons
* Real-Time Intent Detection
* Confidence Score Display
* Local Deployment

---

# 🧠 How Rasa NLU Works

When a user sends a message:

```text
I lost my debit card
```

The message follows this flow:

```text
User Message
      ↓
Streamlit Frontend
      ↓
Rasa REST API
      ↓
NLU Pipeline
      ↓
Intent Detection
      ↓
Confidence Prediction
      ↓
Response Generation
      ↓
User Interface
```

Example Prediction:

```text
Intent:
card_lost

Confidence:
0.98
```

The predicted intent is then mapped to predefined banking responses inside the Rasa domain configuration.

---

# 🏗️ System Architecture

```text
User
  ↓
Streamlit Frontend
  ↓
Rasa REST API
  ↓
Rasa NLU Pipeline
  ↓
Intent Classification
  ↓
Response Selection
  ↓
Banking Response
```

---

# 🛠️ Technology Stack

| Component           | Technology              |
| ------------------- | ----------------------- |
| Frontend            | Streamlit 1.46.1        |
| NLP Engine          | Rasa Open Source 3.6.21 |
| Intent Classifier   | DIET Classifier         |
| Dialogue Management | Stories + Rules         |
| Language            | Python 3.10.11          |
| Machine Learning    | Scikit-Learn            |
| Data Processing     | Pandas                  |
| Numerical Computing | NumPy                   |

---

# 📁 Project Structure

```text
xeria-bank-assistant/
│
├── app.py
├── requirements.txt
├── README.md
│
└── rasa_project/
    ├── config.yml
    ├── domain.yml
    ├── data/
    │   ├── nlu.yml
    │   ├── stories.yml
    │   └── rules.yml
    │
    └── models/
```

---

# ▶️ Running The Project

### Train the Model

```bash
cd rasa_project

rasa data validate

rasa train
```

### Start Rasa Server

```bash
rasa run --enable-api --cors "*"
```

### Launch Streamlit

```bash
streamlit run app.py
```

---

# 💬 Example Queries

```text
check my balance

open a savings account

home loan details

i lost my debit card

forgot my pin

nearest branch

register complaint

connect me with bank staff
```

---

# 📚 What I Learned

This project provided practical experience in:

* Natural Language Understanding (NLU)
* Intent Classification
* Conversational AI Design
* Rasa Open Source Framework
* Streamlit Application Development
* REST API Integration
* YAML-Based Training Pipelines
* Banking Chatbot Development
* Human Escalation Workflows

---

# 👨‍💻 Author

### Rohit Bisht

**B.Sc. Data Science & Artificial Intelligence**

Project Type: Conversational AI

Domain: Banking

Technology: Rasa NLU + Streamlit

Status: Completed ✅
