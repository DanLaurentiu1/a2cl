"use client";
import { Problem } from "@/app/domain/Problem";
import { Plan } from "../../domain/Plan";
import { Handle, NodeProps, Position } from "reactflow";
import PlanContext from "@/app/context/PlanContext";
import { useContext, useState } from "react";
export default function ProblemNode({
  data: { planId, problemId, name, acceptanceRate, difficulty },
}: NodeProps<{
  planId: number;
  problemId: number;
  name: string;
  acceptanceRate: number;
  difficulty: number;
}>) {
  const context = useContext(PlanContext);

  if (!context) {
    throw new Error("PlansList must be used within a PlanProvider");
  }

  const { planRepository } = context;
  const [isChecked, setIsChecked] = useState(
    planRepository.getPlanById(planId)?.getProblemById(problemId)?.[0] ?? false
  );
  let borderColorClass: string;
  switch (difficulty) {
    case 0:
      borderColorClass = "border-green-500";
      break;
    case 1:
      borderColorClass = "border-orange-500";
      break;
    case 2:
      borderColorClass = "border-red-500";
      break;
    default:
      borderColorClass = "border-gray-500";
  }
  return (
    <div
      className={`bg-lightgrey border-2 ${borderColorClass} rounded-lg p-4 w-80 flex justify-between items-center`}
    >
      <Handle
        type="target"
        position={Position.Top}
        id={`target-${problemId}`}
        className="opacity-0"
      />
      <p className="text-white font-semibold">
        {problemId.toString() + ". " + name}
      </p>
      <label className="relative flex items-center cursor-pointer">
        <input
          type="checkbox"
          className="sr-only peer"
          checked={isChecked}
          onChange={(e) => {
            planRepository.checkProblem(planId, problemId);
            setIsChecked(e.target.checked);
          }}
        />
        <div className="w-5 h-5 rounded border-2 border-white peer-checked:bg-lightgreen transition-colors"></div>
      </label>
      <Handle
        type="source"
        position={Position.Bottom}
        id={`source-${problemId}`}
        className="opacity-0"
      />
    </div>
  );
}
