import { planServerRepository } from "@/app/lib/backend/repositories/PlanServerRepository";
import { Problem, ProblemJSON } from "@/app/lib/domain/Problem";
import { NextResponse } from "next/server";

export async function GET(_: Request, { params }: { params: { id: string } }) {
  try {
    const { id } = await params;
    const planId = Number(id);
    const plan = planServerRepository.getPlanById(Number(planId));
    return NextResponse.json(plan);
  } catch (error) {
    return NextResponse.json({ error: "Plan not found" }, { status: 404 });
  }
}

export async function PATCH(
  request: Request,
  { params }: { params: { id: string } }
) {
  try {
    const { id } = await params;
    const planId = Number(id);
    if (isNaN(planId)) {
      return NextResponse.json({ error: "Invalid plan ID" }, { status: 400 });
    }
    const requestBody = await request.json();
    if (!requestBody?.problems || !Array.isArray(requestBody.problems)) {
      return NextResponse.json(
        { error: "Invalid problems format" },
        { status: 400 }
      );
    }
    const problems: Array<[boolean, Problem]> = requestBody.problems.map(
      (item: [boolean, ProblemJSON]) => {
        const [completed, problemJson] = item;
        return [completed, Problem.fromJSON(problemJson)];
      }
    );

    const updatedPlan = await planServerRepository.updatePlanProblems(
      planId,
      problems
    );

    return NextResponse.json(updatedPlan);
  } catch (error) {
    console.error("PATCH error:", error);
    return NextResponse.json(
      { error: error instanceof Error ? error.message : "Update failed" },
      { status: 500 }
    );
  }
}

export async function DELETE(
  _: Request,
  { params }: { params: { id: string } }
) {
  try {
    const { id } = await params;
    const planId = Number(id);
    planServerRepository.deletePlan(Number(planId));
    return new Response(null, { status: 204 });
  } catch (error) {
    return NextResponse.json({ error: "Delete failed" }, { status: 500 });
  }
}
