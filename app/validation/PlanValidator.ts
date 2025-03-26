import { Plan } from "../domain/Plan";

export class PlanValidator {
  static validatePlan(plan: Partial<Plan>): void {
    if (!/^(?! )[A-Za-z0-9]+(?: [A-Za-z0-9]+)*$/.test(plan.title!)) {
      throw new Error("Invalid characters in the title");
    }
    if (plan.title!.length > 100) {
      throw new Error("Plan name must be ≤ 100 characters");
    }
  }
}
