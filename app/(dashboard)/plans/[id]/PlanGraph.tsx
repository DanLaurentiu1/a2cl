"use client";
import React from "react";
import { Plan } from "@/app/domain/Plan";
import ProblemNode from "@/app/ui/problems/ProblemNode";
import { Edge, Node } from "reactflow";
import ReactFlow from "reactflow";
import "reactflow/dist/style.css";
const nodeTypes = {
  problemNode: ProblemNode,
};

export default function PlanGraph(plan: Plan | undefined) {
  const nodes: Node[] = [];
  const edges: Edge[] = [];
  let centerY = window.innerWidth / 2 - 800;
  const centerX = window.innerWidth / 2 - 300;
  plan?.problems.forEach((problem) => {
    nodes.push({
      id: problem[1].id.toString(),
      type: "problemNode",
      position: { x: centerX, y: centerY },
      data: {
        number: problem[1].id,
        name: problem[1].name,
        acceptanceRate: problem[1].acceptanceRate,
        difficulty: problem[1].difficulty,
      },
    });
    centerY += 125;
  });

  for (let i = 0; i < plan!.problems.length - 1; i++) {
    const current = plan!.problems[i][1];
    const next = plan!.problems[i + 1][1];

    edges.push({
      id: `${current.id}-${next.id}`,
      source: current.id.toString(),
      target: next.id.toString(),
      style: { stroke: "#10B981", strokeWidth: 2, width: 12 },
    });
  }

  return (
    <ReactFlow
      nodes={nodes}
      edges={edges}
      nodeTypes={nodeTypes}
      fitView
    ></ReactFlow>
  );
}
