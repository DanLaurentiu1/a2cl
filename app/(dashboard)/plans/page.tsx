"use client";
import { useContext } from "react";
import PlanCard from "@/app/ui/plans/PlanCard";
import PlanContext from "@/app/context/PlanContext";

export default function AllPlans() {
  const context = useContext(PlanContext);

  if (!context) {
    throw new Error("PlansList must be used within a PlanProvider");
  }

  const { planRepository } = context;
  return (
    <div className="p-8 grid grid-cols-4 gap-32">
      {planRepository.getPlans().map((plan) => PlanCard(plan))}
    </div>
  );
}
