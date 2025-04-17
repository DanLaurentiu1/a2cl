import { planServerRepository } from "@/app/lib/backend/repositories/PlanServerRepository";
import { Plan, PlanJSON } from "@/app/lib/domain/Plan";
import { NextResponse } from "next/server";

export async function GET() {
  try {
    const plans = planServerRepository.getAllPlans();
    return NextResponse.json(plans);
  } catch (error) {
    return NextResponse.json(
      { error: "Internal Server Error" },
      { status: 500 }
    );
  }
}

export async function POST(request: Request) {
  try {
    const jsonData: PlanJSON = await request.json();
    const planData: Plan = Plan.fromJSON(jsonData);
    const newPlan: Plan = planServerRepository.addPlan(planData);
    return NextResponse.json(newPlan.toJSON(), { status: 201 });
  } catch (error) {
    return NextResponse.json(
      { error: error instanceof Error ? error.message : "Validation failed" },
      { status: 400 }
    );
  }
}
