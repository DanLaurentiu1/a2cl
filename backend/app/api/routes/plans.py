import traceback
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import text
from app.api.schemas.schemas import PlanJSON, UpdatePlanProblemsRequest
from app.core.domain import Plan, Problem
from app.core.repository.PlanServerRepository import PlanServerRepository
from app.core.database.database import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix="/api/plans", tags=["plans"])

def get_repository(db: Session = Depends(get_db)):
    return PlanServerRepository(db)
    
@router.get("/", response_model=List[PlanJSON])
async def get_plans(repo: PlanServerRepository = Depends(get_repository)):
    try:
        plans = repo.get_all_plans()
        return [plan.to_json() for plan in plans]
    except Exception as e:
        print(f"FULL ERROR: {e}\n{traceback.format_exc()}")
        raise HTTPException(500, detail="Internal Server Error")

@router.post("/", response_model=PlanJSON, status_code=201)
async def create_plan(
    plan_data: PlanJSON,
    repo: PlanServerRepository = Depends(get_repository)
):
    try:
        plan = Plan.from_json(plan_data)
        new_plan = repo.add_plan(plan)
        return new_plan.to_json()
    except ValueError as e:
        raise HTTPException(400, detail=str(e))
    except Exception as e:
        raise HTTPException(500, detail="Internal Server Error")
    
@router.get("/{plan_id}", response_model=PlanJSON)
async def get_plan(
    plan_id: int,
    repo: PlanServerRepository = Depends(get_repository)
):
    try:
        plan = repo.get_plan(plan_id)
        if not plan:
            raise HTTPException(status_code=404, detail="Plan not found")
        return plan.to_json()
    except Exception as e:
        raise HTTPException(500, detail="Internal Server Error")
    
@router.patch("/{plan_id}", response_model=PlanJSON)
async def update_plan_problems(
    plan_id: int,
    request: UpdatePlanProblemsRequest,
    repo: PlanServerRepository = Depends(get_repository)
):
    try:
        problems_data = request.problems
        problems = [
            (completed, Problem.from_json(problem_json))
            for completed, problem_json in problems_data
        ]
        updated_plan = repo.update_plan_problems(plan_id, problems)
        if not updated_plan:
            raise HTTPException(404, detail="Plan not found")
            
        return updated_plan.to_json()
    except HTTPException:
        raise
    except ValueError as e:
        raise HTTPException(400, detail=str(e))
    except Exception as e:
        print(f"PATCH error: {str(e)}")
        raise HTTPException(500, detail="Update failed")

@router.delete("/{plan_id}")
async def delete_plan(
    plan_id: int,
    repo: PlanServerRepository = Depends(get_repository)
):
    try:
        if not repo.delete_plan(plan_id):
            raise HTTPException(404, detail="Plan not found")
    except HTTPException:
        raise
    except Exception as e:
        print(f"DELETE error: {str(e)}")
        raise HTTPException(500, detail="Delete failed")