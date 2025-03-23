"use client";
import React, { useState } from "react";
import PlanContext from "./PlanContext";
import { planRepository } from "../repository/PlanRepository";
import { Plan } from "../domain/Plan";

type PlanProviderProps = {
  children: React.ReactNode;
};

export const PlanProvider = ({ children }: PlanProviderProps) => {
  const [plans, setPlans] = useState<Array<Plan>>(
    planRepository.instantiatePlans()
  );

  planRepository.initialize(setPlans);

  return (
    <PlanContext.Provider value={{ planRepository, plans }}>
      {children}
    </PlanContext.Provider>
  );
};
