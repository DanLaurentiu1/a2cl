import { Plan } from "../../domain/Plan";
import { INITIAL_PLANS } from "../../shared/data/plans";
import { planValidator } from "../../shared/validation/PlanValidator";

class PlanStore {
  private plans: Plan[];
  private nextId: number;

  constructor(initialData: Plan[]) {
    this.plans = [...initialData];
    this.nextId = Math.max(...initialData.map((p) => p.id)) + 1;
  }

  getAll() {
    return [...this.plans];
  }

  getById(id: number): Plan {
    const result = this.plans.find((plan) => plan.id === id);
    if (result === undefined) {
      throw new Error();
    }
    return result;
  }

  add(plan: Omit<Plan, "id">): void {
    this.plans.push(
      new Plan(this.nextId++, plan.title, plan.profile, plan.problems)
    );
  }

  update(id: number, updates: Partial<Plan>): void {
    const index = this.plans.findIndex((plan) => plan.id === id);
    if (index === -1) {
      throw new Error();
    }

    const current = this.plans[index];
    const updatedPlan = new Plan(
      updates.id ?? current.id,
      updates.title ?? current.title,
      updates.profile ?? current.profile,
      updates.problems ?? current.problems
    );

    this.plans[index] = updatedPlan;
  }

  delete(id: number): void {
    this.plans = this.plans.filter((plan) => plan.id !== id);
  }
}

export class PlanServerRepository {
  private planStore: PlanStore;

  constructor() {
    this.planStore = new PlanStore(JSON.parse(JSON.stringify(INITIAL_PLANS)));
  }

  getAllPlans(): Array<Plan> {
    return this.planStore.getAll();
  }

  getPlanById(id: number): Plan {
    return this.planStore.getById(id);
  }

  createPlan(planData: Omit<Plan, "id">): void {
    planValidator.validatePlan(planData);
    this.planStore.add(planData);
  }

  toggleProblemStatus(planId: number, problemId: number): void {
    const plan = this.planStore.getById(planId);
    if (!plan) throw new Error("Plan not found");

    const updatedProblems = plan.problems.map((p) =>
      p[1].id === problemId ? { ...p, isCompleted: !p[0] } : p
    );

    this.planStore.update(planId, { problems: updatedProblems });
  }

  deletePlan(id: number) {
    const exists = this.planStore.getById(id);
    if (!exists) return false;

    return this.planStore.delete(id);
  }
}
export const planServerRepository = new PlanServerRepository();
