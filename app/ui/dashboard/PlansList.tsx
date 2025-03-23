"use client";
import { useContext } from "react";
import Link from "next/link";
import PlanContext from "@/app/context/PlanContext";
import { FaTrash } from "react-icons/fa";

export default function PlansList() {
  const context = useContext(PlanContext);

  if (!context) {
    throw new Error("PlansList must be used within a PlanProvider");
  }

  const { planRepository } = context;

  const handleDelete = (planId: number) => {
    planRepository.deletePlan(planId);
  };
  return (
    <div className="flex flex-col flex-grow overflow-auto m-1">
      <ul className="p-1">
        {planRepository.getPlans().map((plan) => (
          <li
            key={plan.id}
            className="flex justify-between items-center mb-2 text-white bg-lightgrey backdrop-blur-sm p-2 rounded-2xl hover:bg-white/20 transition-all duration-10 cursor-pointer"
          >
            <Link href={`/plans/${plan.id}`}>
              <span className="text-white">{plan.title}</span>
            </Link>
            <button
              className="text-white bg-lightgrey p-2 rounded-3xl border-2 border-lightgreen font-semibold flex items-center justify-center hover:border-orange transition-all duration-200"
              aria-label="Delete plan"
              onClick={() => handleDelete(plan.id)}
            >
              <FaTrash className="w-3 h-3" />
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}
