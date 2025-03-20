"use client";
import React, { useEffect } from "react";
import { Plan } from "@/app/domain/Plan";
import ProblemNode from "@/app/ui/problems/ProblemNode";
import { Edge, Node } from "reactflow";
import ReactFlow, { Controls, Background } from "reactflow";
import "reactflow/dist/style.css";
const nodeTypes = {
  problemNode: ProblemNode,
};

export default function PlanGraph(plan: Plan | undefined) {
  const nodes: Node[] = [];
  let startOfNextNodeY: number = 0;
  const centerX = window.innerWidth / 2 - 300;
  plan?.problems.forEach((problem) => {
    nodes.push({
      id: problem[1].id.toString(),
      type: "problemNode",
      position: { x: centerX, y: startOfNextNodeY },
      data: {
        number: problem[1].id,
        name: problem[1].name,
        acceptanceRate: problem[1].acceptanceRate,
        difficulty: problem[1].difficulty,
      },
    });

    startOfNextNodeY += 100;
  });
  return <ReactFlow nodes={nodes} nodeTypes={nodeTypes}></ReactFlow>;
}
