Bom, consegui os seguintes resultados:

│In [53]: classifiers.classify(df[columns],df.shot_made_flag)
~                                                                                        │GaussianNB : 0.6497270442182915
~                                                                                        │LogisticRegression : 0.6413601793689935
~                                                                                        │LinearSVC : 0.6091349785987149
~                                                                                        │RandomForestClassifier : 0.7307451453896434

Usando as seguintes colunas:

columns
~                                                                                        │Out[56]: ['action_type_number', 'shot_distance', 'is_3pt', 'playoffs', 'points_game']

Com essa submissao eu fiquei com 15.



columns = ['action_type_number', 'combined_shot_type_number', 'season_number', 'shot_zone_area_number', 'shot_zone_basic_number', 'shot_zone_range_number', 'opponent_number', 'playoffs', 'minutes_remaining', 'period', 'rate', 'points_game', 'points_attempt']
