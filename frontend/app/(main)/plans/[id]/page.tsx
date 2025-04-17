"use client";
import { usePlans } from "@/app/components/providers/PlanProvider";
import PlanGraph from "./PlanGraph";
import { use } from "react";

export default function PlanPage({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const { plans, loading, error } = usePlans();

  if (loading) return <div>Loading plan...</div>;
  if (error) return <div>Error: {error}</div>;

  const { id } = use(params);
  const plan = plans.find((plan) => plan.id === Number(id));

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
