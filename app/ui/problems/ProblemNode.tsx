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
  const borderColor: Map<number, string> = new Map();
  borderColor.set(0, "green-500");
  borderColor.set(1, "orange");
  borderColor.set(2, "red-500 ");

  return (
    <div
      className={`bg-lightgrey border-2 border-${borderColor.get(
        difficulty
      )} rounded-lg p-4 w-80`}
    >
      <p className="text-white font-semibold">
        {number.toString() + ". " + name}
      </p>
    </div>
  );
}
