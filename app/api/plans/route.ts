import { planServerRepository } from "@/app/lib/backend/repositories/PlanServerRepository";
import { Plan } from "@/app/lib/domain/Plan";
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
    const planData: Omit<Plan, "id"> = await request.json();
    const newPlan = planServerRepository.addPlan(planData);
    return NextResponse.json(newPlan, { status: 201 });
  } catch (error) {
    return NextResponse.json(
      { error: error instanceof Error ? error.message : "Validation failed" },
      { status: 400 }
    );
  }
}
