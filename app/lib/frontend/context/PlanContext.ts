import { createContext } from "react";
import { Problem } from "../../domain/Problem";
import { Plan } from "../../domain/Plan";

type PlanContextType = {
  plans: Array<Plan>;
  loading: boolean;
  error: string | null;
  addPlan: (planData: Plan) => Promise<void>;
  updatePlanProblems: (
    planId: number,
    problems: Array<[boolean, Problem]>
  ) => Promise<void>;
  deletePlan: (planId: number) => Promise<void>;
  getPlans: () => Promise<void>;
  getPlanById: (id: number) => Plan;
};

export const PlanContext = createContext<PlanContextType | undefined>(
  undefined
);
