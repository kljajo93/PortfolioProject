select * from CovidDeaths
order by 3,4
select * from CovidVaccinations
order by 3,4

select location, date, total_cases, new_cases, total_deaths, population
from CovidDeaths

order by 1,2

--
select location, date, total_cases,  total_deaths, (total_deaths/total_cases)*100 as death_pct
from CovidDeaths
where location like'%croatia%'
order by 1,2

--total cases vs population
select location, date, total_cases,  population, (total_cases/population)*100 as InfectedPct
from CovidDeaths
where location like'%croatia%'
order by 1,2

select location,  MAX(total_cases),  population, MAX((total_cases/population))*100 as TotalPctInfected
from CovidDeaths
Group by population, location
order by TotalPctInfected Desc

-- countries with the most deaths per population
select location,  MAX(cast(total_deaths as int))as totalDeaths
from CovidDeaths
where continent is not null 
Group by  location
order by totalDeaths Desc

--Deaths by continent
select location,  MAX(cast(total_deaths as int))as totalDeaths
from CovidDeaths
where continent is  null 
Group by  location
order by totalDeaths Desc

--Deaths by date

select date,  SUM(cast(new_deaths as int))as totalDeaths, SUM(new_cases) as Totalcases, (SUM(cast(new_deaths as int))/SUM(new_cases))*100 as DeathsPercentage
from CovidDeaths
where continent is not null 
--Group by  date
order by totalDeaths Desc

select   SUM(cast(new_deaths as int))as totalDeaths, SUM(new_cases) as Totalcases, (SUM(cast(new_deaths as int))/SUM(new_cases))*100 as DeathsPercentage
from CovidDeaths
where continent is not null 
--Group by  date
order by totalDeaths Desc

with cte_vac (continent, location, date, population, new_vaccinations, rollingPeoplevac)
as (
select dea.continent, dea.location,dea.date, population, vac.new_vaccinations,
sum(cast(new_vaccinations as int)) over (partition by dea.location order by dea.location,
dea.date) as rollingPeoplevac
from CovidDeaths dea
join  CovidVaccinations vac
on dea.location = vac.location
and dea.date= vac.date
where dea.continent is not null 
--order by 2,3
)
select *, (rollingPeoplevac/population)*100
from cte_vac

DROP TABLE IF EXISTS #VacTemp
CREATE TABLE #VacTemp(
continent nvarchar(50),
Location nvarchar(255),
Date datetime,
Population numeric,
New_vaccinations numeric,
RollingPeopleVaccinated numeric
)
Insert into #VacTemp
select dea.continent, dea.location,dea.date, population, vac.new_vaccinations,
sum(cast(new_vaccinations as int)) over (partition by dea.location order by dea.location,
dea.date) as rollingPeoplevac
from CovidDeaths dea
join  CovidVaccinations vac
on dea.location = vac.location
and dea.date= vac.date
where dea.continent is not null 


select *, (RollingPeopleVaccinated/population)*100
from #VacTemp

Create View PercentPopulationVaccinated as
select dea.continent, dea.location,dea.date, population, vac.new_vaccinations,
sum(cast(new_vaccinations as int)) over (partition by dea.location order by dea.location,
dea.date) as rollingPeoplevac
from CovidDeaths dea
join  CovidVaccinations vac
on dea.location = vac.location
and dea.date= vac.date
where dea.continent is not null