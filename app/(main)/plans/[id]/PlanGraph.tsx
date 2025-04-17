"use client";
import React from "react";
import { Plan } from "@/app/lib/domain/Plan";
import { Edge, Node } from "reactflow";
import ReactFlow from "reactflow";
import "reactflow/dist/style.css";
import ProblemNode from "@/app/components/ui/problems/ProblemNode";
import ProblemEdge from "@/app/components/ui/problems/ProblemEdge";
const nodeTypes = {
  problemNode: ProblemNode,
};

const edgeTypes = {
  problemEdge: ProblemEdge,
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
        planId: plan.id,
        problemId: problem[1].id,
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
      sourceHandle: `source-${current.id.toString()}`,
      targetHandle: `target-${next.id.toString()}`,
      type: "problemEdge",
    });
  }

  return (
    <ReactFlow
      nodes={nodes}
      edges={edges}
      nodeTypes={nodeTypes}
      edgeTypes={edgeTypes}
      fitView
    ></ReactFlow>
  );
}
