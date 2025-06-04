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

  const problemCountMap = new Map<string, number>();
  const nodeIds: string[] = [];

  plan?.problems.forEach((problem, _) => {
    const problemId = problem[1].id.toString();
    const count = problemCountMap.get(problemId) || 0;
    problemCountMap.set(problemId, count + 1);
    const uniqueNodeId = `${problemId}-${count}`;
    nodeIds.push(uniqueNodeId);
    nodes.push({
      id: uniqueNodeId,
      type: "problemNode",
      position: { x: centerX, y: centerY },
      data: {
        planId: plan.id,
        problemId: problem[1].id,
        name: problem[1].name,
        acceptanceRate: problem[1].acceptanceRate,
        difficulty: problem[1].difficulty
      },
    });
    centerY += 125;
  });

  for (let i = 0; i < (plan?.problems.length || 0) - 1; i++) {
    const sourceId = nodeIds[i];
    const targetId = nodeIds[i + 1];

    edges.push({
      id: `edge-${i}-${sourceId}-${targetId}`,
      source: sourceId,
      target: targetId,
      sourceHandle: `source-${sourceId}`,
      targetHandle: `target-${targetId}`,
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
    />
  );
}