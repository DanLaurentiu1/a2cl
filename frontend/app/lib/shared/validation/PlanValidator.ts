import { Plan } from "../../domain/Plan";
import { profileValidator } from "./ProfileValidator";

export class PlanValidator {
  public validatePlan(plan: Omit<Plan, "id">): void {
    this.validatePlanTitle(plan);
    this.validatePlanProfile(plan);
  }

  public validatePlanProfile(plan: Omit<Plan, "id">): void {
    profileValidator.validateProfile(plan.profile);
  }

  public validatePlanTitle(plan: Omit<Plan, "id">): void {
    if (typeof plan.title !== "string") {
      throw new Error("Title must be a string");
    }
    if (!/^(?! )[A-Za-z0-9]+(?: [A-Za-z0-9]+)*$/.test(plan.title)) {
      throw new Error("Invalid characters in the title");
    }
    if (plan.title.length > 100) {
      throw new Error("Plan name must be ≤ 100 characters");
    }
  }
}
export let planValidator = new PlanValidator();
