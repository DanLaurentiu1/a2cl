<h1 align="center">A2CL</h1>
<p align="center"><strong>Full-stack application that helps you organize and optimize your LeetCode problem-solving plans.</strong></p>
</div>

<div align="center">
  <picture>
    <img src="https://github.com/DanLaurentiu1/a2cl/blob/documentation-branch/documents/plans_view_page.png" width="500" height="300" />
  </picture>
</div>


## Overview
asdasd

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

## Project Status
🔴 Archived / No Longer Maintained