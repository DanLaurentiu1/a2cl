import { ApiError } from "next/dist/server/api-utils";
import { Plan, PlanJSON } from "../domain/Plan";
import { Problem } from "../domain/Problem";

export class PlanClientRepository {
  private baseUrl: string = `${process.env.NEXT_PUBLIC_BACKEND_URL}/api/plans/`;

  async getAllPlans(): Promise<Array<Plan>> {
    const response = await fetch(this.baseUrl);
    if (!response.ok) {
      throw new ApiError(500, `Failed to fetch plans: ${response.statusText}`);
    }
    const jsonData: Array<PlanJSON> = await response.json();
    return jsonData.map((planJson) => Plan.fromJSON(planJson));
  }

  async getPlanById(id: number): Promise<Plan> {
    const response = await fetch(`${this.baseUrl}${id}`);
    if (!response.ok) {
      if (response.status === 404) {
        throw new ApiError(404, `Plan with ID ${id} not found`);
      }
      throw new ApiError(500, `Failed to fetch plan: ${response.statusText}`);
    }
    const jsonData: PlanJSON = await response.json();
    return Plan.fromJSON(jsonData);
  }

  async addPlan(planData: Plan): Promise<Plan> {
    console.log(JSON.stringify(planData.toJSON()));
    const response = await fetch(this.baseUrl, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(planData.toJSON()),
    });

    if (!response.ok) {
      const errorData = await response.json();
      throw new ApiError(
        response.status,
        errorData.message || "Failed to create plan"
      );
    }
    const jsonData: PlanJSON = await response.json();
    return Plan.fromJSON(jsonData);
  }

  async updatePlanProblems(
    planId: number,
    newProblems: Array<[boolean, Problem]>
  ): Promise<Plan> {
    const problemsJson = newProblems.map(([completed, problem]) => [
      completed,
      problem.toJSON(),
    ]);

    const response = await fetch(`${this.baseUrl}${planId}`, {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ problems: problemsJson }),
    });

    if (!response.ok) {
      const errorData = await response.json();
      throw new ApiError(
        response.status,
        errorData.message || "Failed to update plan problems"
      );
    }
    const jsonData: PlanJSON = await response.json();
    return Plan.fromJSON(jsonData);
  }

  async deletePlan(id: number): Promise<void> {
    const response = await fetch(`${this.baseUrl}${id}`, {
      method: "DELETE",
    });

    if (!response.ok) {
      const errorData = await response.json();
      throw new ApiError(
        response.status,
        errorData.message || "Failed to delete plan"
      );
    }
  }
}

export const planClientRepository = new PlanClientRepository();
