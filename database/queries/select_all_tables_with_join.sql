select l_t.name, m_t.name, t_t.name, tu_t.name
from languages l_t
join manuales m_t ON m_t.language_id = l_t.id
join topics t_t ON t_t.manuale_id = m_t.id
join tutorials tu_t ON tu_t.topic_id = t_t.id
