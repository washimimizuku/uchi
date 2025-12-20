// @ts-check
import { defineConfig } from 'astro/config';

// https://astro.build/config
export default defineConfig({
  content: {
    collections: {
      blog: {
        type: 'content',
        schema: ({ z }) => z.object({
          title: z.string(),
          description: z.string(),
          publishDate: z.date(),
          author: z.string().optional(),
          tags: z.array(z.string()).optional(),
        })
      },
      pages: {
        type: 'content',
        schema: ({ z }) => z.object({
          title: z.string(),
          description: z.string().optional(),
          template: z.string().default('page'),
        })
      }
    }
  }
});
