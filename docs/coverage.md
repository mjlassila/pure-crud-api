# SDK coverage

970 operations: 928 generated, 21 partial, 21 unsupported.

Every operation is recorded in `coverage.json`. Generated means a module exists without a generation warning; it does not imply live verification. Partial binary downloads expose raw bytes through `sync_detailed().content` but lack a 200 parser. Unsupported wildcard uploads have no module. Changing `*/*` to a concrete MIME type would narrow the contract, so preprocessing does not do that. The smallest future extension is a generator template supporting arbitrary binary request media types.

| Operation | Status | Cause |
| --- | --- | --- |
| `activity_fileUploads` (PUT `/activities/file-uploads`) | unsupported | Wildcard binary request body is unsupported by generator |
| `activity_getFile` (GET `/activities/{uuid}/files/{fileId}`) | partial | Wildcard binary 200 response has no generated parser; sync_detailed().content contains bytes |
| `application_fileUploads` (PUT `/applications/file-uploads`) | unsupported | Wildcard binary request body is unsupported by generator |
| `application_getFile` (GET `/applications/{uuid}/files/{fileId}`) | partial | Wildcard binary 200 response has no generated parser; sync_detailed().content contains bytes |
| `award_fileUploads` (PUT `/awards/file-uploads`) | unsupported | Wildcard binary request body is unsupported by generator |
| `award_getFile` (GET `/awards/{uuid}/files/{fileId}`) | partial | Wildcard binary 200 response has no generated parser; sync_detailed().content contains bytes |
| `contract_fileUploads` (PUT `/contracts/file-uploads`) | unsupported | Wildcard binary request body is unsupported by generator |
| `contract_getFile` (GET `/contracts/{uuid}/files/{fileId}`) | partial | Wildcard binary 200 response has no generated parser; sync_detailed().content contains bytes |
| `course_fileUploads` (PUT `/courses/file-uploads`) | unsupported | Wildcard binary request body is unsupported by generator |
| `course_getFile` (GET `/courses/{uuid}/files/{fileId}`) | partial | Wildcard binary 200 response has no generated parser; sync_detailed().content contains bytes |
| `dataSet_fileUploads` (PUT `/data-sets/file-uploads`) | unsupported | Wildcard binary request body is unsupported by generator |
| `dataSet_getFile` (GET `/data-sets/{uuid}/files/{fileId}`) | partial | Wildcard binary 200 response has no generated parser; sync_detailed().content contains bytes |
| `equipment_fileUploads` (PUT `/equipment/file-uploads`) | unsupported | Wildcard binary request body is unsupported by generator |
| `equipment_getFile` (GET `/equipment/{uuid}/files/{fileId}`) | partial | Wildcard binary 200 response has no generated parser; sync_detailed().content contains bytes |
| `ethicalReview_fileUploads` (PUT `/ethical-reviews/file-uploads`) | unsupported | Wildcard binary request body is unsupported by generator |
| `ethicalReview_getFile` (GET `/ethical-reviews/{uuid}/files/{fileId}`) | partial | Wildcard binary 200 response has no generated parser; sync_detailed().content contains bytes |
| `externalOrganization_fileUploads` (PUT `/external-organizations/file-uploads`) | unsupported | Wildcard binary request body is unsupported by generator |
| `externalOrganization_getFile` (GET `/external-organizations/{uuid}/files/{fileId}`) | partial | Wildcard binary 200 response has no generated parser; sync_detailed().content contains bytes |
| `externalPerson_fileUploads` (PUT `/external-persons/file-uploads`) | unsupported | Wildcard binary request body is unsupported by generator |
| `externalPerson_getFile` (GET `/external-persons/{uuid}/files/{fileId}`) | partial | Wildcard binary 200 response has no generated parser; sync_detailed().content contains bytes |
| `fundingOpportunity_fileUploads` (PUT `/funding-opportunities/file-uploads`) | unsupported | Wildcard binary request body is unsupported by generator |
| `fundingOpportunity_getFile` (GET `/funding-opportunities/{uuid}/files/{fileId}`) | partial | Wildcard binary 200 response has no generated parser; sync_detailed().content contains bytes |
| `impact_fileUploads` (PUT `/impacts/file-uploads`) | unsupported | Wildcard binary request body is unsupported by generator |
| `impact_getFile` (GET `/impacts/{uuid}/files/{fileId}`) | partial | Wildcard binary 200 response has no generated parser; sync_detailed().content contains bytes |
| `milestone_fileUploads` (PUT `/milestones/file-uploads`) | unsupported | Wildcard binary request body is unsupported by generator |
| `milestone_getFile` (GET `/milestones/{uuid}/files/{fileId}`) | partial | Wildcard binary 200 response has no generated parser; sync_detailed().content contains bytes |
| `organization_fileUploads` (PUT `/organizations/file-uploads`) | unsupported | Wildcard binary request body is unsupported by generator |
| `organization_getFile` (GET `/organizations/{uuid}/files/{fileId}`) | partial | Wildcard binary 200 response has no generated parser; sync_detailed().content contains bytes |
| `person_fileUploads` (PUT `/persons/file-uploads`) | unsupported | Wildcard binary request body is unsupported by generator |
| `person_getFile` (GET `/persons/{uuid}/files/{fileId}`) | partial | Wildcard binary 200 response has no generated parser; sync_detailed().content contains bytes |
| `pressmedia_fileUploads` (PUT `/pressmedia/file-uploads`) | unsupported | Wildcard binary request body is unsupported by generator |
| `pressmedia_getFile` (GET `/pressmedia/{uuid}/files/{fileId}`) | partial | Wildcard binary 200 response has no generated parser; sync_detailed().content contains bytes |
| `prize_fileUploads` (PUT `/prizes/file-uploads`) | unsupported | Wildcard binary request body is unsupported by generator |
| `prize_getFile` (GET `/prizes/{uuid}/files/{fileId}`) | partial | Wildcard binary 200 response has no generated parser; sync_detailed().content contains bytes |
| `project_fileUploads` (PUT `/projects/file-uploads`) | unsupported | Wildcard binary request body is unsupported by generator |
| `project_getFile` (GET `/projects/{uuid}/files/{fileId}`) | partial | Wildcard binary 200 response has no generated parser; sync_detailed().content contains bytes |
| `researchOutput_fileUploads` (PUT `/research-outputs/file-uploads`) | unsupported | Wildcard binary request body is unsupported by generator |
| `researchOutput_getFile` (GET `/research-outputs/{uuid}/files/{fileId}`) | partial | Wildcard binary 200 response has no generated parser; sync_detailed().content contains bytes |
| `studentProject_fileUploads` (PUT `/student-projects/file-uploads`) | unsupported | Wildcard binary request body is unsupported by generator |
| `studentProject_getFile` (GET `/student-projects/{uuid}/files/{fileId}`) | partial | Wildcard binary 200 response has no generated parser; sync_detailed().content contains bytes |
| `studentThesis_fileUploads` (PUT `/student-theses/file-uploads`) | unsupported | Wildcard binary request body is unsupported by generator |
| `studentThesis_getFile` (GET `/student-theses/{uuid}/files/{fileId}`) | partial | Wildcard binary 200 response has no generated parser; sync_detailed().content contains bytes |
