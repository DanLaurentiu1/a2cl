"use client";
import { plans } from "@/app/domain/data";
import PlanGraph from "./PlanGraph";
import { use } from "react";

export default function PlanPage({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const { id } = use(params);
  const plan = plans.find((plan) => plan.id === Number(id));
  return (
    <div className="w-full h-full p-6 rounded-lg items-center">
      {PlanGraph(plan)}
    </div>
  );
}
