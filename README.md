<h1 align="center">A2CL</h1>
<p align="center"><strong>Full-stack application that helps you organize and optimize your LeetCode problem-solving plans.</strong></p>

<div align="center">
  <picture>
    <img src="https://github.com/DanLaurentiu1/a2cl/blob/documentation-branch/documents/plans_view_page.png" width="450" height="400" />
  </picture>
</div>


## Overview
### What?
This application provides an interface for creating and managing learning plans, specifically for the LeetCode platform. Additionally, we use multiple reinforcement learning based algorithms to automatically generate practice problem-sets. The user specifies which topics they want to practice, and a problem-set is curated for them.

### Why?
On their own, the problem-sets are perhaps slightly inferior to already existing, human-made plans. Our approach shines when the topics specified either vary wildly in difficulty (Advanced Dynamic Programming vs Two Pointers) or are uncommonly mixed together (Graph vs Combinatorics). Through experience, our algorithm automatically visits prerequisite sub-topics and techniques, creating plausible plans for a mix of multiple topics.

### How?
The project uses [Next.js](https://nextjs.org/) with [TailwindCSS](https://tailwindcss.com/) for the front-end and [FastAPI](https://fastapi.tiangolo.com/) for the back-end. User plans are stored in a [PostgreSQL](https://www.postgresql.org/) database using the [SQLAlchemy ORM](https://www.sqlalchemy.org/). Model's skeleton is built with [Gymnasium](https://gymnasium.farama.org/index.html) and monitored using [Stable-Baselines3](https://stable-baselines3.readthedocs.io/en/master/) callbacks. Our approaches are benchmarked against existing Stable-Baselines3 models. The entire project is deployed in production: the front-end is hosted on [Vercel](https://vercel.com/), and the back-end and database are managed via [Render](https://render.com/). <br> <br> <br>

<p align="center">Below are diagrams for the architecture (<strong>left</strong>) and model-flow (<strong>right</strong>)</p>

<div align="center">
  <picture>
    <img src="https://github.com/DanLaurentiu1/a2cl/blob/documentation-branch/documents/architecture_diagram.png" width="400" height="400" />
  </picture>
  <picture>
    <img src="https://github.com/DanLaurentiu1/a2cl/blob/documentation-branch/documents/model_flow_diagram.png" width="400" height="400" />
  </picture>
</div>

## Installation (open-source)
```bash
# copy the project locally
git clone https://github.com/DanLaurentiu1/a2cl.git
```

### Front-End Setup:
```bash
# create environment file with placeholder values (fine for running locally)
cd frontend
echo "NEXT_PUBLIC_BACKEND_URL=http://localhost:8000" > .env

# install dependencies and start
npm install pnpm
pnpm install
pnpm dev
```

### Back-End Setup:
```bash
# create the virtual environment and activate
cd backend
python -m venv venv
venv\Scripts\activate

# create environment file with placeholder values (fine for running locally) 
echo "DB_URL=\nCORS_ORIGINS=http://localhost:3000" > .env

# install dependencies and start
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Repository Structure
```
a2cl/
├── frontend/
│   ├── app/
│   │   ├── (main)                  # main page and dynamic routes for all entities
│   │   ├── components              # all UI components
│   │   ├── lib                     # domain, repository, validation
│   ├── .env.local
│   ├── package.json
│   └── ...
├── backend/
│   ├── app/
│   │   ├── api                     # requests routes and JSON schemas
│   │   ├── core                    # domain, repository, validation and database models 
│   │   ├── model                   # the model used, data, logs, checkpoints, plots and other utilities
│   │   ├── tests                   # unit tests
│   │   ├── main.py                 # fastAPI starting point
│   ├── .env
│   ├── requirements.txt
│   └── ...
```
## More details
The full [thesis document](https://github.com/DanLaurentiu1/a2cl/blob/documentation-branch/documents/Thesis.pdf) presents in-depth details about implementation, performance, architecture and more. <br>

A high-level [overview](https://github.com/DanLaurentiu1/a2cl/blob/documentation-branch/documents/Thesis%20Presentation.pdf) is also available.

## Project Status
🔴 Archived / No Longer Maintained