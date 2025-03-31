"use client";
import PlanGraph from "./PlanGraph";
import { use, useContext } from "react";
import PlanContext from "@/app/context/PlanContext";

export default function PlanPage({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const context = useContext(PlanContext);

  if (!context) {
    throw new Error("PlansList must be used within a PlanProvider");
  }

  const { planRepository } = context;
  const { id } = use(params);
  const plan = planRepository.getPlans().find((plan) => plan.id === Number(id));

  if (!plan) {
    return (
      <div className="flex justify-center items-center w-full h-full p-6 rounded-lg">
        <div className="flex flex-col w-1/4 bg-lightgrey p-6 rounded-lg justify-center items-center">
          <p className="text-white text-2xl font-semibold">
            Plan does not exist
          </p>
        </div>
      </div>
    );
  }

  return (
    <div className="w-full h-full p-6 rounded-lg items-center">
      {PlanGraph(plan)}
    </div>
  );
}
