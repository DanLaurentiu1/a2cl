import { createContext } from "react";
import { PlanRepository } from "../repository/PlanRepository";
import { Plan } from "../domain/Plan";

type PlanContextType = {
  plans: Array<Plan>;
  planRepository: PlanRepository;
};

const PlanContext = createContext<PlanContextType | null>(null);

export default PlanContext;
