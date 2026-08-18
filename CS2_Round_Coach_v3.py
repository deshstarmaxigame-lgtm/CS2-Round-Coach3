import tkinter as tk
from tkinter import ttk
import random

MAPS = ["Ancient", "Anubis", "Dust II", "Inferno", "Mirage", "Nuke", "Cache"]

# Public/pro-style concepts transformed into original coaching instructions.
# Not copied from private team playbooks.
TACTICS = {
"Mirage": {
"T": [
("ДЕФОЛТ → МИД → A SPLIT", "Не отдаём ранние смерти. 2 Mid, 1 Ramp, 1 Palace, 1 Apps. Забрать Mid и Connector, затем синхронно A."),
("A EXEC", "3 Ramp + 2 Palace. Smoke CT/Jungle/Stairs, две флешки на вход, выход плотной пятёркой."),
("MID → B SPLIT", "2 Mid/Short + 3 Apps. Сначала контроль Mid, затем одновременный выход Short + Apps."),
("FAST B", "4–5 игроков через Apps с флешками. Цель — быстрый размен и установка без остановки."),
("FAKE B → A", "Показать B utility и контакт, удержать CT на B, затем быстро собрать Ramp/Palace на A."),
("ПАССИВНЫЙ DEFAULT → ПОЗДНИЙ EXEC", "Распределиться по карте, ловить пуши, сохранить гранаты до 0:45–0:35 и выбрать слабый сайт."),
],
"CT": [
("СТАНДАРТ 2-1-2", "2 A, 1 Mid, 2 B. Не отдавать первый фраг бесплатно; Mid даёт раннюю информацию и быстрые ротации."),
("MID PRESSURE", "Давление Mid с флешкой/поддержкой, затем отход. Цель — получить информацию, не умереть первым."),
("ANTI-RUSH", "Ранние HE/флешки на вероятную точку давления, затем пассивная оборона и игра на трейды."),
("ПАССИВНЫЙ RETAKE", "Не форсировать дуэли. Сохранить utility для retake и принимать решение после подтверждения сайта."),
]
},
"Inferno": {
"T": [
("BANANA CONTROL → B", "3 игрока Banana с utility, 2 держат Mid/Apps. После контроля — B execute."),
("A SPLIT", "2 Apps + 2 Mid + 1 Banana lurk. Давление Mid/Apps, затем синхронный выход A."),
("DEFAULT → LATE A", "Контроль Banana/Mid/Apps без ранней авантюры. На 0:45 выбрать A по информации."),
("FAST B", "Плотный выход B после молотов/флешек. Первые два игрока работают на трейд, остальные сразу закрывают ретейк-линии."),
("FAKE B → A", "Создать шум на Banana и utility B, затем быстро собрать Apps/Mid и выйти A."),
],
"CT": [
("2-1-2 + BANANA CONTROL", "2 B с utility на Banana, 1 Mid, 2 A. Не отдавать Banana бесплатно."),
("АГРЕССИВНАЯ BANANA → ОТХОД", "Ранний контроль Banana с поддержкой, после получения информации — отход и сохранение жизни."),
("ПАССИВНЫЙ B RETAKE", "Не умирать в Banana. Сохранить molotov/smoke для замедления и играть от retake."),
]
},
"Nuke": {
"T": [
("OUTSIDE SMOKES → SECRET", "Закрыть ключевые линии Outside, один игрок давит Secret, остальные создают давление Ramp/A."),
("RAMP HIT", "3 игрока Ramp с флешками, 2 поддерживают/контролируют Outside. После входа быстро закрепиться Lower."),
("DEFAULT → OUTSIDE", "Spread Outside/Ramp/House. Наказать агрессивную оборону и принять late-round решение."),
("A EXEC", "Собрать 4–5 игроков на A после Outside/Ramp давления, изолировать Heaven/CT и войти одновременно."),
],
"CT": [
("СТАНДАРТ 2-1-2", "2 A, 1 Outside, 2 Ramp/Lower. Outside игрок даёт информацию и не отдаёт бесплатный пик."),
("OUTSIDE INFO", "Ранний utility/info Outside, затем отход. Не превращать информационный контакт в бессмысленную дуэль."),
("RAMP HOLD", "Плотная защита Ramp с флешкой на первый контакт; после контакта сохранить численное преимущество."),
]
},
"Ancient": {
"T": [
("MID CONTROL → B SPLIT", "2–3 Mid/Donut + 2 B Main. Забрать пространство и синхронно открыть B с двух направлений."),
("A EXEC", "A Main + Mid/Donut давление. Smoke CT/Donut, флешки на вход и быстрый plant."),
("DEFAULT → B", "2 B, 2 Mid, 1 A lurk. Ловить агрессивные CT и выбирать B при слабом Mid/Donut."),
("FAST B", "Плотная атака B Main с флешками, первые два игрока работают только на трейд."),
("FAKE A → B", "Показать A utility/контакт, заставить ротацию, затем быстро собрать B Main + Mid."),
],
"CT": [
("2-1-2", "2 A, 1 Mid, 2 B. Mid игрок играет на информацию и быстро сообщает о Donut/Temple."),
("MID CONTEST → FALLBACK", "Ранний contest Mid с поддержкой, затем отход при сильном utility T."),
("ПАССИВНЫЙ B", "Не отдавать B первым дуэлянтам. Играть от utility и retake, если T собрали сильный execute."),
]
},
"Anubis": {
"T": [
("MID → B SPLIT", "Контроль Mid + B Main, затем split B. Важно синхронизировать две группы."),
("A EXEC", "3 A Main + 2 Mid. Utility на ключевые позиции и плотный выход без пауз."),
("DEFAULT → LATE B", "Распределиться A/Mid/B Main, дождаться CT агрессии и поздно собрать B."),
("FAST A", "Быстрый A с флешками и трейдами. Не останавливаться после первого контакта."),
("FAKE B → A", "Показать B pressure, удержать ротацию, затем быстро собрать A."),
],
"CT": [
("2-1-2", "2 A, 1 Mid, 2 B. Mid игрок сохраняет жизнь и сообщает о split-потенциале."),
("PASSIVE INFO", "Минимум ранних рисков. Собирать звук/визуальную информацию и ротировать только по подтверждению."),
("B RETAKE", "Не отдавать лишние смерти. Сохранить utility для остановки plant/retake."),
]
},
"Dust II": {
"T": [
("LONG → A", "3 Long + 2 Short/Mid. Забрать Long, закрыть CT и выйти A через две точки."),
("CAT SPLIT", "2 Long + 2 Cat + 1 Mid/B lurk. Синхронный выход A после получения контроля."),
("FAST B", "3 Tunnel + 2 Mid support. Флешки на выход, первые два игрока играют на трейд."),
("DEFAULT → LATE A", "Контроль Long/Mid/Tunnel без ранней драки, затем решение по слабой точке CT."),
("FAKE LONG → B", "Показать Long pressure, заставить A ротировать, затем быстро закрыть B."),
],
"CT": [
("2-1-2", "2 A, 1 Mid, 2 B. Mid игрок не отдаёт ранний пик без поддержки."),
("LONG DENIAL", "Ранний utility на Long, затем отход к сильным позициям и игра на трейды."),
("PASSIVE MID", "Сохранить AWP/utility, получить информацию через безопасный peek и не переигрывать."),
]
},
"Cache": {
"T": [
("A MAIN → A EXEC", "3 A Main + 2 Mid. Smoke CT/Highway, флешки и синхронный выход."),
("MID → B SPLIT", "Контроль Mid + B Main, затем split B после вынужденной ротации."),
("DEFAULT → LATE A", "Распределиться A/Mid/B, ловить пуши и поздно собрать A."),
("FAST B", "Плотный B Main hit с флешками и трейдами, без остановки после первого контакта."),
("FAKE B → A", "Создать давление B utility, заставить CT сместиться, затем быстрый A."),
],
"CT": [
("2-1-2", "2 A, 1 Mid, 2 B. Mid игрок даёт раннюю информацию и не умирает первым."),
("MID PRESSURE", "Ранний contest Mid с поддержкой, затем отход и сохранение utility."),
("PASSIVE RETAKE", "Сдерживать первые контакты, не отдавать лишние смерти, играть от retake."),
]
}
}

STYLES = ["Неизвестен", "Агрессивный", "Пассивный", "Часто пушит Mid", "Часто пушит A", "Часто пушит B", "Часто играет retake"]

class Coach(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CS2 Round Coach — Premier")
        self.geometry("980x800")
        self.minsize(900, 700)
        self.round_no = 1
        self.score_t = 0
        self.score_ct = 0
        self.last = "Нет данных"
        self.loss_streak = 0
        self.win_streak = 0
        self.econ_t = 800
        self.econ_ct = 800
        self.last_tactical = None
        self.build()
        self.generate()

    def build(self):
        ttk.Label(self, text="CS2 ROUND COACH", font=("Segoe UI", 24, "bold")).pack(anchor="w")
        ttk.Label(self, text="Тактический помощник для Premier • русский язык • адаптация по счёту, серии и экономике",
                  font=("Segoe UI", 10)).pack(anchor="w", pady=(0, 12))
        f = ttk.Frame(self); f.pack(fill="x")

        self.map_var = tk.StringVar(value="Mirage")
        self.side_var = tk.StringVar(value="T")
        self.style_var = tk.StringVar(value="Неизвестен")
        self.t_var = tk.StringVar(value="0")
        self.ct_var = tk.StringVar(value="0")
        self.money_override = tk.StringVar(value="Авто")

        fields = [
            ("Карта", self.map_var, MAPS),
            ("Сторона", self.side_var, ["T", "CT"]),
            ("Стиль соперника", self.style_var, STYLES),
        ]
        for i, (label, var, vals) in enumerate(fields):
            ttk.Label(f, text=label).grid(row=0, column=i*2, sticky="w", padx=5, pady=4)
            ttk.Combobox(f, textvariable=var, values=vals, state="readonly", width=22).grid(row=0, column=i*2+1, padx=5)

        ttk.Label(f, text="Счёт T").grid(row=1, column=0, sticky="w", padx=5, pady=4)
        ttk.Entry(f, textvariable=self.t_var, width=24).grid(row=1, column=1, padx=5)
        ttk.Label(f, text="Счёт CT").grid(row=1, column=2, sticky="w", padx=5)
        ttk.Entry(f, textvariable=self.ct_var, width=24).grid(row=1, column=3, padx=5)
        ttk.Label(f, text="Экономика").grid(row=1, column=4, sticky="w", padx=5)
        ttk.Label(f, text="Автоматически", foreground="green").grid(row=1, column=5, sticky="w", padx=5)

        b = ttk.Frame(self); b.pack(fill="x", pady=12)
        ttk.Button(b, text="🎯 Новая тактика", command=self.generate).pack(side="left", padx=4)
        ttk.Button(b, text="✅ ВЫИГРАЛИ РАУНД", command=lambda: self.finish(True)).pack(side="left", padx=4)
        ttk.Button(b, text="❌ ПРОИГРАЛИ РАУНД", command=lambda: self.finish(False)).pack(side="left", padx=4)
        ttk.Button(b, text="↺ Новый матч", command=self.reset).pack(side="right", padx=4)

        self.out = tk.Text(self, font=("Consolas", 12), wrap="word", height=35)
        self.out.pack(fill="both", expand=True)

    def get_scores(self):
        try: return int(self.t_var.get()), int(self.ct_var.get())
        except: return 0, 0

    def economy(self):
        side_money = self.econ_t if self.side_var.get() == "T" else self.econ_ct
        if side_money < 2000: return "🔴 ECO — сохраняем деньги"
        if side_money < 3000: return "🟠 LIGHT BUY — дешёвый закуп + utility"
        if side_money < 4200: return "🟡 SEMI BUY — закуп по ролям"
        return "🟢 FULL BUY — rifle + utility"

    def match_state(self):
        t, ct = self.get_scores()
        diff = (t-ct) if self.side_var.get() == "T" else (ct-t)
        if diff <= -6 or self.loss_streak >= 3:
            return "🚨 КРИЗИС: большой минус / серия поражений. Меняем темп, не повторяем предыдущую схему."
        if diff <= -3 or self.loss_streak == 2:
            return "⚠️ МИНУС: играем стабильнее, но добавляем одну смену темпа."
        if diff >= 6 or self.win_streak >= 3:
            return "🟢 БОЛЬШОЙ ПЛЮС: сохраняем давление и не дарим сопернику оружие/пики."
        return "🟡 РАБОЧИЙ РАУНД: default → информация → mid-round решение."

    def choose_tactic(self):
        m, side = self.map_var.get(), self.side_var.get()
        pool = TACTICS[m][side]
        # Avoid exact repeat when possible.
        candidates = [x for x in pool if x[0] != self.last_tactical] or pool
        return random.choice(candidates)

    def adaptation(self):
        style = self.style_var.get()
        if style == "Агрессивный": return "🪤 Наказывать раннюю агрессию: anti-push + трейд, затем использовать освободившуюся зону."
        if style == "Пассивный": return "🧱 Забираем пространство utility, не спешим с фраги, вынуждаем ротации."
        if style == "Часто пушит Mid": return "🎯 Оставить anti-push. После повторного пуша — наказать трейдом и продолжить в противоположную сторону."
        if style == "Часто пушит A": return "🎯 Ловим A-пуш, затем используем освободившийся A/CT control для split."
        if style == "Часто пушит B": return "🎯 Ловим B-пуш, затем быстро переносим давление на A."
        if style == "Часто играет retake": return "⏱️ Быстрее занимать плент и сохранять utility на пост-плэнт; не давать бесплатные дуэли на подходе."
        return "🔎 Собираем информацию первые 20–30 секунд и принимаем решение по реакции CT."

    def generate(self):
        t, ct = self.get_scores()
        state = self.match_state()
        eco = self.economy()
        name, plan = self.choose_tactic()
        # Crisis modifier: prefer a different style than previous round.
        if (self.loss_streak >= 2 or (t-ct <= -6 if self.side_var.get()=="T" else ct-t <= -6)):
            crisis = "\n🚨 ПРИ БОЛЬШОМ МИНУСЕ: не повторять прошлую тактику. Если прошлый раунд был slow — ускориться; если был rush — сыграть default с late execute."
        else: crisis = ""
        self.last_tactical = name
        text = f"""РАУНД {self.round_no}  |  {self.map_var.get()}  |  {self.side_var.get()}
СЧЁТ: {t} : {ct}
Последний результат: {self.last}
Серия побед: {self.win_streak}   Серия поражений: {self.loss_streak}

{state}

💰 ЭКОНОМИКА
{eco}
(Расчёт внутренний и приблизительный: программа учитывает результаты раундов, но не читает деньги из памяти CS2.)

🎯 ТАКТИКА
{name}
{plan}
{crisis}

🧠 СОПЕРНИК
{self.adaptation()}

📌 ГЛАВНОЕ ПРАВИЛО
Не отдавать одиночные смерти. Первый контакт проигран — остановиться, сохранить игроков и принять новое mid-round решение.

ℹ️ Тактическая база построена на публичных профессиональных принципах и открытых разборах CS2; закрытые командные материалы не используются.
"""
        self.out.delete("1.0", "end")
        self.out.insert("1.0", text)

    def finish(self, won):
        side = self.side_var.get()
        self.last = "ПОБЕДА" if won else "ПОРАЖЕНИЕ"
        if won:
            self.win_streak += 1; self.loss_streak = 0
            if side == "T": self.score_t += 1
            else: self.score_ct += 1
            # Approximate team money model: win bonus grows; not exact per-player economy.
            if side == "T": self.econ_t = min(16000, self.econ_t + 3250)
            else: self.econ_ct = min(16000, self.econ_ct + 3250)
        else:
            self.loss_streak += 1; self.win_streak = 0
            if side == "T": self.econ_t = min(16000, self.econ_t + min(3400, 1400 + self.loss_streak*500))
            else: self.econ_ct = min(16000, self.econ_ct + min(3400, 1400 + self.loss_streak*500))
        self.t_var.set(str(self.score_t)); self.ct_var.set(str(self.score_ct))
        self.round_no += 1
        self.generate()

    def reset(self):
        self.round_no=1; self.score_t=0; self.score_ct=0; self.last="Нет данных"; self.loss_streak=0; self.win_streak=0; self.econ_t=800; self.econ_ct=800; self.last_tactical=None
        self.t_var.set("0"); self.ct_var.set("0"); self.generate()

if __name__ == "__main__":
    Coach().mainloop()
