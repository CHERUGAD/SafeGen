# SafeGen
Prevent deepfakes. Block impersonation. Protect brand identity. SafeGen is an AI safety gateway that wraps around any generative model to detect, restrict, and log harmful or unauthorized content.

# SafeGen – Ethical AI Guardrails for Prompts and Content

**SafeGen** is a security-focused AI middleware platform that protects against harmful or unauthorized generation of AI content (text, images, video) involving real people, brands, or sensitive assets.

## 🔐 What It Does

- ❌ Blocks harmful prompts (e.g., impersonation, fake news, deepfakes)
- 🧠 Filters unauthorized requests based on company-registered data
- ✅ Allows only safe, ethical generation of content
- 📊 Offers companies a dashboard to register their assets and protect them from misuse

## 🚀 Use Cases

| User | Use Case |
|------|----------|
| LLM App Developer | Integrate SafeGen API to reject bad prompts |
| AI Video/Photo Tool | Prevent generation of celebrity or brand-based fakes |
| Brand/Company | Protect CEO faces, logos, product blueprints from being used |
| Schools | Prevent students from generating offensive or impersonating content |

## 🧠 Components

- `prompt_guard.py` – Blocks prompts with harmful intent
- `output_filter.py` *(coming soon)* – Detects post-generation risks
- `consent_registry.py` *(coming soon)* – Tracks allowed brands/assets
- `api/` – FastAPI server to interact with SafeGen
- `frontend/` *(planned)* – Dashboard for companies

## 💡 Business Model (SaaS)

- Free for personal / dev use (limited)
- Paid plans for companies to:
  - Register assets
  - Access misuse reports
  - Integrate via API keys

## 🛠 Tech Stack

- Python, FastAPI
- Regex + LLM-based filtering
- GitHub Actions (CI)
- Vision model (for image scan) *(planned)*
- Stripe billing *(planned)*

---

## 📂 Project Structure

SafeGen/
├── app/
│ ├── prompt_guard.py
│ ├── consent_registry.py # (to build)
│ ├── output_filter.py # (to build)
│
├── api/
│ └── main.py # FastAPI server
│
├── frontend/ # Streamlit or ReactJS dashboard (future)
│
├── README.md
└── requirements.txt