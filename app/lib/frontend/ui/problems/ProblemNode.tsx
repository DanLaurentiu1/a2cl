"use client";
import { Problem } from "@/app/lib/domain/Problem";
import { Handle, NodeProps, Position } from "reactflow";
import { useContext, useState } from "react";
import { usePlans } from "../../context/PlanProvider";
import { Plan } from "@/app/lib/domain/Plan";
export default function ProblemNode({
  data: { planId, problemId, name, acceptanceRate, difficulty },
}: NodeProps<{
  planId: number;
  problemId: number;
  name: string;
  acceptanceRate: number;
  difficulty: number;
}>) {
  const { updatePlanProblems, getPlanById } = usePlans();
  const plan: Plan = getPlanById(planId);
  const currentProblem = plan?.problems.find((p) => p[1].id === problemId);
  const [isChecked, setIsChecked] = useState(currentProblem?.[0] ?? false);

  const handleCheckboxChange = async () => {
    if (!plan) return;

    const newCheckedState = !isChecked;
    setIsChecked(newCheckedState);

    try {
      const updatedProblems = plan.problems.map<[boolean, Problem]>((p) => {
        if (p[1].id === problemId) {
          return [newCheckedState, p[1]];
        }
        return p;
      });

      await updatePlanProblems(planId, updatedProblems);
    } catch (error) {
      setIsChecked(!newCheckedState);
      console.error("Update failed:", error);
    }
  };

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
          onChange={handleCheckboxChange}
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
