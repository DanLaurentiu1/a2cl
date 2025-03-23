"use client";
import { useContext } from "react";
import { plans } from "../../domain/data";
import PlanCard from "@/app/ui/plans/PlanCard";
import PlanContext from "@/app/context/PlanContext";

export default function AllPlans() {
  const context = useContext(PlanContext);

  if (!context) {
    throw new Error("PlansList must be used within a PlanProvider");
  }

  const { planRepository, plans } = context;
  console.log(plans);
  return (
    <div className="p-8 grid grid-cols-4 gap-32">
      {plans.map((plan) => PlanCard(plan))}
    </div>
  );
}
