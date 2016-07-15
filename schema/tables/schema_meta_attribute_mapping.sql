CREATE TABLE `schema_meta_attribute_mapping` (
  `schema_id` int(11) NOT NULL,
  `meta_attr_schema_id` int(11) NOT NULL,
  `created_at` int(11) NOT NULL,
  `updated_at` int(11) NOT NULL,
  KEY `schema_id_index` (`schema_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
