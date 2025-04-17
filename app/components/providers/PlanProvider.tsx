"use client";

import { useContext, useEffect, useState } from "react";
import { PlanContext } from "./PlanContext";
import { Plan } from "@/app/lib/domain/Plan";
import { PlanClientRepository } from "@/app/lib/repositories/PlanClientRepository";
import { Problem } from "@/app/lib/domain/Problem";

export const PlanProvider: React.FC<{ children: React.ReactNode }> = ({
  children,
}) => {
  const [plans, setPlans] = useState<Array<Plan>>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const repo = new PlanClientRepository();
  const getPlans = async () => {
    setLoading(true);
    try {
      const data = await repo.getAllPlans();
      setPlans(data);
      setError(null);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Failed to load plans");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    getPlans();
  }, []);

  const addPlan = async (planData: Plan) => {
    setLoading(true);
    try {
      const newPlan = await repo.addPlan(planData);
      setPlans((prev) => [...prev, newPlan]);
      setError(null);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Failed to create plan");
      throw err;
    } finally {
      setLoading(false);
    }
  };

  const updatePlanProblems = async (
    planId: number,
    problems: Array<[boolean, Problem]>
  ) => {
    setLoading(true);
    try {
      const updatedPlan = await repo.updatePlanProblems(planId, problems);
      setPlans((prev) => prev.map((p) => (p.id === planId ? updatedPlan : p)));
      setError(null);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Failed to update plan");
      throw err;
    } finally {
      setLoading(false);
    }
  };

  const deletePlan = async (planId: number) => {
    setLoading(true);
    try {
      await repo.deletePlan(planId);
      setPlans((prev) => prev.filter((p) => p.id !== planId));
      setError(null);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Failed to delete plan");
      throw err;
    } finally {
      setLoading(false);
    }
  };

  const getPlanById = (id: number): Plan => {
    const plan = plans.find((plan) => plan.id === id);
    if (!plan) throw new Error();
    return plan;
  };

  return (
    <PlanContext.Provider
      value={{
        plans,
        loading,
        error,
        addPlan,
        updatePlanProblems,
        deletePlan,
        getPlans,
        getPlanById,
      }}
    >
      {children}
    </PlanContext.Provider>
  );
};

export const usePlans = () => {
  const context = useContext(PlanContext);
  if (!context) {
    throw new Error("usePlans must be used within a PlanProvider");
  }
  return context;
};
