import { openai } from "./api.js";

async function listFineTunes() {
  try {
    const response = await openai.listFineTunes();
    const jobs = response.data.data.filter((job) => {
      if (job.status !== "cancelled") {
        return {
          object: job.object,
          id: job.id,
          model: job.model,
          status: job.status,
          fine_tuned_model: job.fine_tuned_model,
        };
      }
    });
    console.log(`Pending Jobs:`);
    jobs.map((job) => {
      let msg = `{\n\t"object": ${job.object},\n\t"id": ${job.id},\n\t"model": ${job.model},\n\t"status": ${job.status},\n\t"fine_tuned_model": ${job.fine_tuned_model}\n}`;
      console.log(msg);
    });
  } catch (err) {
    console.log("error:", err);
  }
}

listFineTunes();
