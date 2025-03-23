import { createContext } from "react";
import { PlanRepository } from "../repository/PlanRepository";
import { Plan } from "../domain/Plan";

type PlanContextType = {
  planRepository: PlanRepository;
};

const PlanContext = createContext<PlanContextType | null>(null);

export default PlanContext;
