"use client";
import { Problem } from "@/app/domain/Problem";
import { Plan } from "../../domain/Plan";
import { NodeProps } from "reactflow";
export default function ProblemNode({
  data: { number, name, acceptanceRate, difficulty },
}: NodeProps<{
  number: number;
  name: string;
  acceptanceRate: number;
  difficulty: number;
}>) {
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
      className={`bg-lightgrey border-2 ${borderColorClass} rounded-lg p-4 w-80`}
    >
      <p className="text-white font-semibold">
        {number.toString() + ". " + name}
      </p>
    </div>
  );
}
