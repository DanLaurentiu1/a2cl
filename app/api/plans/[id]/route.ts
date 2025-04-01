import { planServerRepository } from "@/app/lib/backend/repositories/PlanServerRepository";
import { NextResponse } from "next/server";

export async function GET(_: Request, { params }: { params: { id: string } }) {
  try {
    const plan = planServerRepository.getPlanById(Number(params.id));
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
    const { problems } = await request.json();
    const updatedPlan = planServerRepository.updatePlanProblems(
      Number(params.id),
      problems
    );
    return NextResponse.json(updatedPlan);
  } catch (error) {
    return NextResponse.json(
      { error: error instanceof Error ? error.message : "Update failed" },
      { status: 400 }
    );
  }
}

export async function DELETE(
  _: Request,
  { params }: { params: { id: string } }
) {
  try {
    planServerRepository.deletePlan(Number(params.id));
    return new Response(null, { status: 204 });
  } catch (error) {
    return NextResponse.json({ error: "Delete failed" }, { status: 500 });
  }
}
