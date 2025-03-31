import { ApiError } from "next/dist/server/api-utils";
import { Plan } from "../../domain/Plan";

export class PlanClientRepository {
  private baseUrl = "/api/plans";

  async getAllPlans(): Promise<Plan[]> {
    const response = await fetch(this.baseUrl);
    if (!response.ok) {
      throw new ApiError(500, `Failed to fetch plans: ${response.statusText}`);
    }
    return response.json();
  }

  async getPlanById(id: number): Promise<Plan> {
    const response = await fetch(`${this.baseUrl}/${id}`);
    if (!response.ok) {
      if (response.status === 404) {
        throw new ApiError(404, `Plan with ID ${id} not found`);
      }
      throw new ApiError(500, `Failed to fetch plan: ${response.statusText}`);
    }
    return response.json();
  }

  async createPlan(planData: Omit<Plan, "id">): Promise<Plan> {
    const response = await fetch(this.baseUrl, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(planData),
    });

    if (!response.ok) {
      const errorData = await response.json();
      throw new ApiError(
        response.status,
        errorData.message || "Failed to create plan"
      );
    }
    return response.json();
  }

  async toggleProblemStatus(
    planId: number,
    problemId: number,
    newIsCompleted: boolean
  ): Promise<Plan> {
    const response = await fetch(
      `${this.baseUrl}/${planId}/problems/${problemId}`,
      {
        method: "PATCH",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ newIsCompleted }),
      }
    );

    if (!response.ok) {
      const errorData = await response.json();
      throw new ApiError(
        response.status,
        errorData.message || "Failed to toggle problem status"
      );
    }
    return response.json();
  }

  async deletePlan(id: number): Promise<void> {
    const response = await fetch(`${this.baseUrl}/${id}`, {
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
