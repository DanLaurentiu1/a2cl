import { AriaAttributes } from "react";
import { Plan } from "../../domain/Plan";
import { INITIAL_PLANS } from "../../shared/data/plans";
import { planValidator } from "../../shared/validation/PlanValidator";
import { Problem } from "../../domain/Problem";

class PlanStore {
  private plans: Array<Plan>;
  private nextId: number;

  constructor(initialData: Array<Plan>) {
    this.plans = [...initialData];
    this.nextId = Math.max(...initialData.map((p) => p.id)) + 1;
  }

  public getAll(): Array<Plan> {
    return [...this.plans];
  }

  public getById(id: number): Plan {
    const result = this.plans.find((plan) => plan.id === id);
    if (result === undefined) {
      throw new Error();
    }
    return result;
  }

  public add(plan: Omit<Plan, "id">): Plan {
    const newPlan = new Plan(
      this.nextId++,
      plan.title,
      plan.profile,
      plan.problems
    );
    this.plans.push(newPlan);
    return newPlan;
  }

  public update(
    id: number,
    updates: { problems: Array<[boolean, Problem]> }
  ): Plan {
    const index = this.plans.findIndex((plan) => plan.id === id);
    if (index === -1) {
      throw new Error(`Plan with ID ${id} not found`);
    }

    const current = this.plans[index];

    const updatedPlan = new Plan(
      current.id,
      current.title,
      current.profile,
      updates.problems
    );

    this.plans[index] = updatedPlan;
    return updatedPlan;
  }

  public delete(id: number): Array<Plan> {
    this.plans = this.plans.filter((plan) => plan.id !== id);
    return this.plans;
  }
}

export class PlanServerRepository {
  private planStore: PlanStore;

  constructor() {
    this.planStore = new PlanStore(JSON.parse(JSON.stringify(INITIAL_PLANS)));
  }

  public getAllPlans(): Array<Plan> {
    return this.planStore.getAll();
  }

  public getPlanById(id: number): Plan {
    return this.planStore.getById(id);
  }

  public addPlan(planData: Omit<Plan, "id">): Plan {
    planValidator.validatePlan(planData);
    return this.planStore.add(planData);
  }

  public updatePlanProblems(
    planId: number,
    newProblems: Array<[boolean, Problem]>
  ): Plan {
    const plan = this.planStore.getById(planId);
    if (!plan) throw new Error("Plan not found");
    return this.planStore.update(planId, { problems: newProblems });
  }

  public deletePlan(id: number): Array<Plan> {
    const exists = this.planStore.getById(id);
    if (!exists) throw new Error("Plan not found");

    return this.planStore.delete(id);
  }
}
export const planServerRepository = new PlanServerRepository();
